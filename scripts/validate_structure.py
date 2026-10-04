"""Validate project structure and its deliberately limited YAML/JSON metadata."""
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

sys.dont_write_bytecode = True
from build_guides import ROOT, guide_name, project_name, render


def main():
    errors = []
    name = project_name()
    def require(condition, message):
        if not condition:
            errors.append(message)

    for filename in ('README.md', 'README-zh.md', 'LICENSE', 'CHANGELOG.md', 'CONTRIBUTING.md', 'CITATION.cff', 'maintenance-guide-en.md', 'maintenance-guide-zh.md'):
        require((ROOT / filename).is_file(), 'Missing ' + filename)
    reference_sets = []
    for lang in ('en', 'zh'):
        skill = ROOT / lang / (name + '-' + lang)
        entry = skill / 'SKILL.md'
        require(entry.is_file(), 'Missing ' + str(entry.relative_to(ROOT)))
        if not entry.is_file():
            continue
        text = entry.read_text(encoding='utf-8-sig')
        fm = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
        require(bool(fm), 'Missing frontmatter: ' + lang)
        fields = {}
        if fm:
            try:
                for line in fm[1].splitlines():
                    key, value = line.split(':', 1)
                    value = value.strip()
                    fields[key] = json.loads(value) if value.startswith('"') else value
            except (ValueError, json.JSONDecodeError):
                errors.append('Unsupported frontmatter syntax: ' + lang)
        require(set(fields) == {'name', 'description'}, 'Entry needs exactly name and description: ' + lang)
        require(fields.get('name') == skill.name, 'Skill name/directory mismatch: ' + lang)
        require(bool(fields.get('description')), 'Empty description: ' + lang)
        metadata = skill / 'agents/openai.yaml'
        require(metadata.is_file(), 'Missing UI metadata: ' + lang)
        if metadata.is_file():
            try:
                lines = metadata.read_text(encoding='utf-8-sig').splitlines()
                assert lines[0] == 'interface:'
                ui = {}
                for line in lines[1:]:
                    assert line.startswith('  ') and not line.startswith('    ')
                    key, value = line.strip().split(':', 1)
                    ui[key] = json.loads(value.strip())
                assert set(ui) == {'display_name', 'short_description', 'default_prompt'}
                assert all(isinstance(v, str) and v for v in ui.values())
                assert 25 <= len(ui['short_description']) <= 64
                assert '$' + skill.name in ui['default_prompt']
            except (AssertionError, ValueError, json.JSONDecodeError):
                errors.append('Invalid UI metadata: ' + lang)
        refs = sorted((skill / 'references').rglob('*.md'))
        reference_sets.append({p.relative_to(skill / 'references').as_posix() for p in refs})
        # Every reference must be reachable from the entrypoint through local links.
        reached = set()
        def visit(p):
            p = p.resolve()
            if p in reached or not p.is_file():
                return
            reached.add(p)
            for target in re.findall(r'\]\(([^)]+)\)', p.read_text(encoding='utf-8-sig')):
                if '://' not in target and not target.startswith('#'):
                    q = (p.parent / target.split('#', 1)[0]).resolve()
                    if q.suffix == '.md' and q.is_relative_to(skill.resolve()):
                        visit(q)
        visit(entry)
        for ref in refs:
            require(ref.resolve() in reached, 'Unrouted reference: ' + ref.relative_to(ROOT).as_posix())
        guide = ROOT / lang / guide_name()
        require(guide.is_file(), 'Missing portable guide: ' + lang)
        if guide.is_file():
            try:
                require(guide.read_text(encoding='utf-8-sig') == render(lang), 'Stale guide: ' + lang)
            except ValueError as exc:
                errors.append(str(exc))
        require((ROOT / lang / 'usage.md').is_file(), 'Missing usage: ' + lang)
    require(len(reference_sets) == 2 and reference_sets[0] == reference_sets[1], 'Language module mismatch')

    for p in ROOT.rglob('*'):
        if '.git' in p.parts or not p.is_file():
            continue
        require('examples' not in p.relative_to(ROOT).parts, 'Examples are excluded from this release')
        if p.suffix != '.md':
            continue
        text = p.read_text(encoding='utf-8-sig')
        for raw in re.findall(r'\]\(([^)]+)\)', text):
            if '://' in raw or raw.startswith('mailto:'):
                continue
            path, _, anchor = unquote(raw).partition('#')
            target = (p.parent / path).resolve() if path else p.resolve()
            require(target.is_relative_to(ROOT.resolve()), 'Link escapes package: ' + raw)
            require(target.is_file(), 'Broken link: ' + p.relative_to(ROOT).as_posix() + ': ' + raw)
            if anchor and target.is_file():
                require(f'id="{anchor}"' in target.read_text(encoding='utf-8-sig'), 'Missing explicit anchor: ' + raw)
        require(not re.search(r'(?<![A-Za-z])[A-Za-z]:[\\/]', text), 'Absolute local path: ' + str(p.relative_to(ROOT)))
        require(not re.search(r'\b(?:sk-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{20,})|BEGIN [A-Z ]*PRIVATE KEY', text), 'Possible secret: ' + str(p.relative_to(ROOT)))
        require(not re.search(r'\[(?:TODO|INSERT|REPLACE)[^\]]*\]', text), 'Unfinished scaffold: ' + str(p.relative_to(ROOT)))

    try:
        citation = json.loads((ROOT / 'CITATION.cff').read_text(encoding='utf-8'))
        require(citation.get('cff-version') == '1.2.0' and citation.get('type') == 'software', 'Invalid CFF identity')
        require(citation.get('repository-code') == 'https://github.com/q1feng/' + name, 'Incorrect citation URL')
        require(citation.get('license') == 'MIT' and bool(citation.get('authors')), 'Incomplete citation metadata')
    except (OSError, ValueError):
        errors.append('Unreadable JSON-compatible CFF metadata')
    if name == 'research-proposal-toolkit':
        manifest = ROOT / 'forge-core-sync.json'
        require(manifest.is_file(), 'Missing Forge snapshot record')
        if manifest.is_file():
            try:
                data = json.loads(manifest.read_text(encoding='utf-8'))
                actual = {p.relative_to(ROOT).as_posix() for lang in ('en','zh') for p in (ROOT/lang/(name+'-'+lang)/'references/forge').glob('*.md')}
                require(set(data['files']) == actual, 'Forge manifest coverage mismatch')
                for path, digest in data['files'].items():
                    p = (ROOT / path).resolve()
                    require(p.is_relative_to(ROOT.resolve()), 'Unsafe snapshot path')
                    if p.is_relative_to(ROOT.resolve()):
                        require(p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == digest, 'Modified Forge snapshot: ' + path)
            except (KeyError, ValueError):
                errors.append('Invalid snapshot record')
    if errors:
        print('\n'.join(errors))
        return 1
    print('PASS: names, metadata, bilingual structure, reference routing, links, guides, citation identity, and package checks')
    print('This is structural validation, not a full YAML/CFF schema, translation, citation-truth, or behavioral evaluation.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
