#!/usr/bin/env python3
"""Hypixel SkyBlock 知識庫查詢工具。

用法：
  python3 kb.py find <關鍵字>        在標題、別名、分類中搜尋（不分大小寫）
  python3 kb.py page <標題或別名> [...]  印出頁面全文（自動解析別名）
  python3 kb.py grep <正規表示式>    全文搜尋，列出命中的頁面與行
  python3 kb.py missing <標題> [...] 檢查頁面是否只在索引、缺本體
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
INDEX_RE = re.compile(r"^- \[\[(.+?)\]\](?: \(aka (.+?)\))?(?: \{(.*?)\})?(?: — (.*))?$")
HEAD_RE = re.compile(r"^# (.+?)\s*$", re.M)


def load_index():
    entries, alias = {}, {}
    with open(os.path.join(ROOT, "index.md"), encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\r\n")
            if " links to page " in line:  # 說明文字，不是條目
                continue
            m = INDEX_RE.match(line)
            if not m:
                continue
            title = m.group(1)
            akas = m.group(2).split(", ") if m.group(2) else []
            entries[title] = (akas, m.group(3) or "", m.group(4) or "")
            alias[title.lower()] = title
            for a in akas:
                alias.setdefault(a.lower(), title)
    return entries, alias


def load_pages(titles):
    """回傳 {標題: (檔案, 起點, 終點)}；只把索引中存在的標題視為頁首，避免內文的 # 標題被誤判。"""
    pages = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "knowledge_*.md"))):
        with open(path, encoding="utf-8") as f:
            text = f.read()
        heads = [(m.start(), m.group(1)) for m in HEAD_RE.finditer(text) if m.group(1) in titles]
        for i, (start, title) in enumerate(heads):
            end = heads[i + 1][0] if i + 1 < len(heads) else len(text)
            pages[title] = (path, start, end)
    return pages


def read_page(loc):
    path, start, end = loc
    with open(path, encoding="utf-8") as f:
        return f.read()[start:end].rstrip()


def resolve(name, alias):
    return alias.get(name.lower())


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return
    cmd, args = sys.argv[1], sys.argv[2:]
    entries, alias = load_index()

    if cmd == "find":
        q = " ".join(args).lower()
        pages = load_pages(set(entries))
        hits = []
        for title, (akas, cats, summary) in entries.items():
            hay = " | ".join([title, *akas, cats]).lower()
            if q in hay:
                score = 0 if title.lower() == q else 1 if title.lower().startswith(q) else 2
                hits.append((score, title, cats, summary))
        for _, title, cats, summary in sorted(hits)[:40]:
            mark = "" if title in pages else "  [缺本體]"
            print(f"- {title}{mark} {{{cats}}}\n    {summary[:160]}")
        print(f"\n共 {len(hits)} 筆" + ("（只顯示前 40）" if len(hits) > 40 else ""))

    elif cmd == "page":
        pages = load_pages(set(entries))
        for name in args:
            title = resolve(name, alias)
            if not title:
                print(f"!! 索引中找不到：{name}（試試 find）")
            elif title not in pages:
                print(f"!! [[{title}]] 在索引中，但知識檔裡沒有頁面本體")
                print("   索引摘要：" + entries[title][2])
            else:
                print(read_page(pages[title]))
            print("\n" + "=" * 60 + "\n")

    elif cmd == "grep":
        pat = re.compile(" ".join(args), re.I)
        pages = load_pages(set(entries))
        n = 0
        for title, loc in pages.items():
            lines = [l for l in read_page(loc).splitlines() if pat.search(l) and not l.startswith("Linked from:")]
            if lines:
                n += 1
                if n <= 30:
                    print(f"[[{title}]]")
                    for l in lines[:3]:
                        print("   " + l[:200])
        print(f"\n共 {n} 頁命中" + ("（只顯示前 30）" if n > 30 else ""))

    elif cmd == "missing":
        pages = load_pages(set(entries))
        for name in args:
            title = resolve(name, alias)
            state = "索引無此頁" if not title else ("有本體" if title in pages else "缺本體")
            print(f"{name} → {title or '-'}：{state}")

    else:
        print(__doc__)


if __name__ == "__main__":
    main()
