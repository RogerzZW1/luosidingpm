#!/usr/bin/env python3
"""本文件用途：生成竞品调研任务的最小执行骨架，帮助整理输入网址、关键词和输出目录；真实浏览器访问优先交给 agent-browser 或 playwright-interactive。"""

from pathlib import Path
import argparse
import json


def main() -> None:
    parser = argparse.ArgumentParser(description='Prepare competitor research task inputs')
    parser.add_argument('--name', required=True, help='竞品名称')
    parser.add_argument('--url', action='append', default=[], help='竞品网址，可重复传入')
    parser.add_argument('--keyword', action='append', default=[], help='调研关键词，可重复传入')
    parser.add_argument('--out-dir', required=True, help='输出目录')
    args = parser.parse_args()

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    manifest = {
        'name': args.name,
        'urls': args.url,
        'keywords': args.keyword,
        'browser_note': '优先使用 agent-browser 或 playwright-interactive 采集网页证据。',
    }
    (out / 'research_manifest.json').write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8'
    )
    (out / 'competitor_research_raw.md').write_text(
        '# 原始证据\n\n- 待补充网页截图、页面路径、Help Center 摘录、搜索结果。\n',
        encoding='utf-8',
    )
    (out / 'competitor_research_summary.md').write_text(
        '# 竞品调研摘要\n\n- 待基于网页证据补充产品定位、核心机制、优劣势和借鉴点。\n',
        encoding='utf-8',
    )
    print(f'已生成竞品调研骨架: {out}')


if __name__ == '__main__':
    main()
