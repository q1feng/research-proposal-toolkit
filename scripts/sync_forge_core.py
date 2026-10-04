"""Explicitly sync/check the embedded core against a local Forge checkout."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULES = ('question-abstraction', 'literature-feedback', 'expansion-decomposition', 'research-taste', 'framework-output')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True, help='Path to the research-question-forge repository')
    parser.add_argument('--check', action='store_true', help='Compare without writing')
    args = parser.parse_args()
    files = {}
    incoming = []
    for lang in ('en', 'zh'):
        for module in MODULES:
            source = args.source / lang / ('research-question-forge-' + lang) / 'references' / (module + '.md')
            if not source.is_file():
                parser.exit(1, 'Missing source module: ' + str(source) + '\n')
            dest = ROOT / lang / ('research-proposal-toolkit-' + lang) / 'references/forge' / source.name
            content = source.read_bytes()
            incoming.append((dest, content))
            files[dest.relative_to(ROOT).as_posix()] = hashlib.sha256(content).hexdigest()
    signature = hashlib.sha256(json.dumps(files, sort_keys=True).encode()).hexdigest()
    manifest = {
        'source_repository': 'https://github.com/q1feng/research-question-forge',
        'snapshot_id': 'sha256:' + signature,
        'source_layout': '{language}/research-question-forge-{language}/references/{module}.md',
        'license': 'MIT',
        'files': files
    }
    path = ROOT / 'forge-core-sync.json'
    if args.check:
        changed = [str(p.relative_to(ROOT)) for p, content in incoming if not p.is_file() or p.read_bytes() != content]
        if not path.is_file() or json.loads(path.read_text(encoding='utf-8')) != manifest:
            changed.append('forge-core-sync.json')
        if changed:
            parser.exit(1, 'Forge core differs: ' + ', '.join(changed) + '\n')
        print('Embedded Forge core and manifest match the supplied source')
    else:
        for dest, content in incoming:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(content)
        path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print('Synced Forge core. Rebuild portable guides and run validation.')


if __name__ == '__main__':
    main()
