"""Build/check portable guides from each language's canonical Skill sources."""
import argparse
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]


def project_name(root=ROOT):
    names = ('research-question-forge', 'research-proposal-toolkit')
    found = [name for name in names if (root / 'en' / (name + '-en') / 'SKILL.md').is_file()]
    if len(found) != 1:
        raise ValueError('Expected one supported bilingual Skill layout')
    return found[0]


def guide_name(root=ROOT):
    return 'question-forge-guide.md' if project_name(root) == 'research-question-forge' else 'proposal-guide.md'


def render(language, root=ROOT):
    skill = root / language / (project_name(root) + '-' + language)
    entry = skill / 'SKILL.md'
    refs = sorted((skill / 'references').rglob('*.md'))
    all_sources = [entry, *refs]
    anchors = {p.resolve(): 'source-' + p.relative_to(skill).as_posix().removesuffix('.md').replace('/', '-').lower() for p in all_sources}
    if language == 'zh':
        intro = '# 完整引导｜免安装中文版\n\n将本文件作为附件，说明观察或想法、已有资料、资源和当前目标。不必先有完整题目。用户要求和学校规范优先。\n\n本文件由同语言 Skill 与全部参考规则生成，可独立用于普通聊天。下文“读取”所指内容已包含在本文件中，直接使用对应章节，无需安装其他 Skill。没有文件工具时提供可保存文本，不声称已经写入文件。\n\n## 内容导航\n'
    else:
        intro = '# Complete guide | Portable English edition\n\nAttach this file and describe your observations or idea, sources, resources, and current goal. A finished title is unnecessary. User and institutional requirements take precedence.\n\nThis guide includes the same-language Skill and all reference rules for ordinary chat use. Instructions to read a resource refer to sections already included here; no other Skill installation is required. Without file tools, provide saveable text rather than claiming files were written.\n\n## Contents\n'
    bodies = []
    toc = []
    for p in all_sources:
        text = p.read_text(encoding='utf-8-sig')
        if p == entry:
            text, count = re.subn(r'\A---\n.*?\n---\n', '', text, count=1, flags=re.S)
            if not count:
                raise ValueError('Missing entry frontmatter')
        title = next(line.lstrip('# ').strip() for line in text.splitlines() if line.startswith('# '))
        anchor = anchors[p.resolve()]
        toc.append(f'- [{title}](#{anchor})')

        def rewrite(match):
            label, url = match.groups()
            if '://' in url or url.startswith('#'):
                return match.group(0)
            target = (p.parent / url.split('#', 1)[0]).resolve()
            if target not in anchors:
                raise ValueError(f'Portable guide has external local dependency: {p.name}: {url}')
            return f'[{label}](#{anchors[target]})'

        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', rewrite, text)
        bodies.append(f'<a id="{anchor}"></a>\n\n{text.strip()}')
    return intro + '\n'.join(toc) + '\n\n---\n\n' + '\n\n---\n\n'.join(bodies) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--language', choices=('en', 'zh', 'all'), default='all')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    languages = ('en', 'zh') if args.language == 'all' else (args.language,)
    stale = []
    for language in languages:
        path = ROOT / language / guide_name()
        expected = render(language)
        if args.check:
            if not path.is_file() or path.read_text(encoding='utf-8-sig') != expected:
                stale.append(path.relative_to(ROOT).as_posix())
        else:
            path.write_text(expected, encoding='utf-8', newline='\n')
            print('Built', path.relative_to(ROOT))
    if stale:
        parser.exit(1, 'Out-of-date guides: ' + ', '.join(stale) + '\n')
    if args.check:
        print('Portable guides match canonical sources:', ', '.join(languages))


if __name__ == '__main__':
    main()
