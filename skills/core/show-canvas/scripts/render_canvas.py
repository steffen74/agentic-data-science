#!/usr/bin/env python3
"""Render a canvas file (COURSE-CANVAS.md, or CANVAS.md of Agentic Data Science) as one HTML page.

The page follows the printed canvas: one column per `## Section` between `---` rules, one card per
`### N. Block 👤|🤖`, then the sections after the last rule (open questions, decision log) below.
Empty blocks show the template's hint and are marked as not decided (👤) or not drafted (🤖).

With a decision log (DECISIONS.md next to the canvas, entries `## YYYY-MM-DD: title` with a line
`**Canvas:** 3, 5` or `**Canvas block:** 3`), each block shows how many decisions touch it, and the decisions newer than the
canvas version date, so a canvas that has fallen behind its log is visible.

  render_canvas.py COURSE-CANVAS.md                     # writes build/canvas.html
  render_canvas.py CANVAS.md --out build/canvas.html --decisions DECISIONS.md
  render_canvas.py COURSE-CANVAS.md --watch             # re-render on every change; the page reloads itself

Standard library only.
"""
import argparse
import datetime
import html
import pathlib
import re
import sys
import time

OWNERS = {"👤": "human", "🤖": "agent"}
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")


def inline(text):
    # Escape first, then the few inline marks canvases use.
    s = html.escape(text, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
               lambda m: f'<a href="{html.escape(m.group(2))}">{m.group(1)}</a>', s)
    return s


def markdown(lines):
    """Paragraphs, lists and quotes: enough for canvas blocks, nothing more."""
    out, para, items = [], [], []

    def flush():
        if para:
            out.append("<p>" + "<br>".join(inline(l) for l in para) + "</p>")
            para.clear()
        if items:
            out.append("<ul>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ul>")
            items.clear()

    for line in lines:
        line = line.rstrip()
        if not line.strip():
            flush()
        elif re.match(r"\s*[-*] ", line):
            if para:
                flush()
            items.append(re.sub(r"^\s*[-*] ", "", line))
        elif line.startswith(">"):
            flush()
            out.append(f"<blockquote>{inline(line.lstrip('> '))}</blockquote>")
        else:
            if items:
                flush()
            para.append(line.strip())
    flush()
    return "\n".join(out)


def strip_comments(text):
    hints = [h.strip() for h in re.findall(r"<!--(.*?)-->", text, re.S)]
    return re.sub(r"<!--.*?-->", "", text, flags=re.S), " ".join(hints)


def parse_canvas(text):
    title, fields, legend = "Canvas", [], ""
    groups, tail = [], []          # groups: columns between rules; tail: sections after the last rule
    current = None                 # the section ("##") being filled
    block = None                   # the block ("###") being filled
    seen_rule = False

    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("# ") and not groups and not seen_rule:
            title = line[2:].strip()
        elif not seen_rule and (m := re.match(r"\*\*(.+?):\*\*\s*(.*)", line)):
            fields.append((m.group(1), strip_comments(m.group(2))[0].strip()))
        elif not seen_rule and line.startswith("> Owners:"):
            legend = line[len("> Owners:"):].strip()
        elif line.strip() == "---":
            seen_rule = True
            block = None
            current = None
        elif line.startswith("## "):
            current = {"name": line[3:].strip(), "blocks": [], "lines": []}
            block = None
            groups.append(current)
        elif line.startswith("### ") and current is not None:
            m = re.match(r"###\s+(\d+)\.?\s+(.*?)\s*(👤|🤖)?\s*$", line)
            number, name, owner = (m.group(1), m.group(2), m.group(3)) if m else ("", line[4:], None)
            block = {"number": number, "name": name, "owner": OWNERS.get(owner), "lines": []}
            current["blocks"].append(block)
        elif block is not None:
            block["lines"].append(line)
        elif current is not None:
            current["lines"].append(line)

    # Sections without blocks after the columns (open questions, decision log) go below the grid.
    while groups and not groups[-1]["blocks"]:
        tail.insert(0, groups.pop())
    for g in groups + tail:
        for b in g["blocks"]:
            body, b["hint"] = strip_comments("\n".join(b["lines"]))
            b["html"], b["empty"] = markdown(body.splitlines()), not body.strip()
        body, g["hint"] = strip_comments("\n".join(g["lines"]))
        g["html"], g["empty"] = markdown(body.splitlines()), not body.strip()
    return {"title": title, "fields": fields, "legend": legend, "columns": groups, "tail": tail}


def parse_decisions(path):
    if not path or not path.exists():
        return []
    text, _ = strip_comments(path.read_text(encoding="utf-8"))
    decisions = []
    for chunk in re.split(r"^## ", text, flags=re.M)[1:]:
        head, _, body = chunk.partition("\n")
        date = DATE.search(head)
        title = head.split(":", 1)[1].strip() if ":" in head else head.strip()
        blocks = re.search(r"\*\*Canvas(?: blocks?)?:\*\*\s*(.+)", body)
        decisions.append({"date": date.group(0) if date else "", "title": title,
                          "blocks": set(re.findall(r"\d+", blocks.group(1))) if blocks else set()})
    return decisions


def version_date(fields):
    for key, value in fields:
        if key.lower() in ("version", "updated", "last update") and (m := DATE.search(value)):
            return m.group(0)
    return ""


def card(b, decisions, since, decider):
    touching = [d for d in decisions if b["number"] in d["blocks"]]
    newer = [d for d in touching if since and d["date"] > since]
    owner = b["owner"] or "human"
    badge = {"human": f"{decider.capitalize()} decides", "agent": "Agent drafts"}[owner]
    state = ""
    if b["empty"]:
        state = '<p class="state">' + ("Not decided yet" if owner == "human" else "Not drafted yet") + "</p>"
    meta = []
    if touching:
        meta.append(f'{len(touching)} decision{"s" if len(touching) != 1 else ""}')
    if newer:
        titles = "&#10;".join(html.escape(f'{d["date"]}: {d["title"]}') for d in newer)
        meta.append(f'<span class="newer" title="{titles}">{len(newer)} newer than the canvas</span>')
    hint = f' title="{html.escape(b["hint"])}"' if b["hint"] else ""
    body = b["html"] if not b["empty"] else f'<p class="hint">{html.escape(b["hint"])}</p>'
    return f"""<section class="block {owner}{' empty' if b['empty'] else ''}"{hint}>
  <header><h3><span class="num">{b['number']}</span> {inline(b['name'])}</h3><span class="badge">{badge}</span></header>
  {state}<div class="body">{body}</div>
  {'<footer>' + ' · '.join(meta) + '</footer>' if meta else ''}
</section>"""


def render(canvas, decisions, source, watch):
    since = version_date(canvas["fields"])
    decider = "instructor" if "instructor" in canvas["legend"] else "human"
    rows = max((len(c["blocks"]) for c in canvas["columns"]), default=1)
    columns = []
    for c in canvas["columns"]:
        cards = []
        for i, b in enumerate(c["blocks"]):
            span = rows - i if i == len(c["blocks"]) - 1 else 1   # the last block fills its column
            cards.append(f'<div style="grid-row: span {span}">{card(b, decisions, since, decider)}</div>')
        columns.append(f'<div class="column"><h2>{inline(c["name"])}</h2>'
                       f'<div class="cards" style="grid-template-rows: repeat({rows}, auto)">{"".join(cards)}</div></div>')

    tail = []
    for t in canvas["tail"]:
        if "decision" in t["name"].lower() and decisions:
            items = "".join(
                f'<li><time>{d["date"]}</time> {inline(d["title"])}'
                f'{" <span class=blocks>" + ", ".join(sorted(d["blocks"], key=int)) + "</span>" if d["blocks"] else ""}'
                f'{" <span class=newer>new</span>" if since and d["date"] > since else ""}</li>'
                for d in decisions[:8])
            more = f'<p class="hint">{len(decisions) - 8} older decisions in the log.</p>' if len(decisions) > 8 else ""
            body = f"<ul class=log>{items}</ul>{more}"
        elif t["empty"]:
            body = f'<p class="hint">{html.escape(t["hint"]) or "Nothing yet."}</p>'
        else:
            body = t["html"]
        tail.append(f'<section class="note"><h3>{inline(t["name"])}</h3>{body}</section>')

    filled = sum(not b["empty"] for c in canvas["columns"] for b in c["blocks"])
    total = sum(len(c["blocks"]) for c in canvas["columns"])
    fields = "".join(f"<div><dt>{inline(k)}</dt><dd>{inline(v) or '–'}</dd></div>" for k, v in canvas["fields"])
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    refresh = '<meta http-equiv="refresh" content="3">' if watch else ""
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">{refresh}
<title>{html.escape(canvas['title'])}</title>
<style>{CSS}</style></head>
<body>
<header class="top">
  <div><h1>{inline(canvas['title'])}</h1>
  <p class="sub">{filled} of {total} blocks filled{' · version ' + since if since else ''}</p></div>
  <dl>{fields}</dl>
</header>
<main class="grid" style="grid-template-columns: repeat({len(columns)}, minmax(0, 1fr))">{''.join(columns)}</main>
<div class="tail">{''.join(tail)}</div>
<footer class="legend">
  <span><i class="sw human"></i>{decider.capitalize()} decides</span>
  <span><i class="sw agent"></i>Agent drafts, {decider} approves</span>
  <span class="src">Rendered from <code>{html.escape(source.name)}</code> · {stamp}</span>
</footer>
</body></html>
"""


CSS = """
:root { --bg:#fff; --ink:#2C2C2A; --muted:#5F5E5A; --rule:#B4B2A9;
  --h-bg:#EEEDFE; --h-line:#534AB7; --h-ink:#3C3489; --a-bg:#E1F5EE; --a-line:#0F6E56; --a-ink:#085041;
  --n-bg:#F1EFE8; --n-line:#888780; --warn:#B4531F; }
@media (prefers-color-scheme: dark) { :root { --bg:#1B1B1A; --ink:#E8E6DF; --muted:#A6A49C; --rule:#4A4944;
  --h-bg:#26234A; --h-line:#8F87E8; --h-ink:#CFCBFF; --a-bg:#12352C; --a-line:#4CB894; --a-ink:#BFEBDC;
  --n-bg:#2A2926; --n-line:#77756E; --warn:#F0A06A; } }
* { box-sizing: border-box; }
body { margin: 0; padding: 24px 30px; background: var(--bg); color: var(--ink);
  font: 13px/1.45 Helvetica, Arial, sans-serif; }
.top { display: flex; justify-content: space-between; gap: 24px; flex-wrap: wrap; align-items: flex-start; }
h1 { margin: 0; font-size: 26px; }
.sub { margin: 4px 0 0; color: var(--muted); }
dl { display: flex; gap: 28px; margin: 0; flex-wrap: wrap; }
dt { font-size: 11px; color: var(--muted); } dd { margin: 2px 0 0; border-top: 1px solid var(--rule); padding-top: 3px; }
.grid { display: grid; gap: 18px; margin-top: 18px; }
.column h2 { font-size: 15px; margin: 0 0 8px; }
.cards { display: grid; gap: 12px; height: calc(100% - 28px); }
.cards > div { display: flex; } .block { flex: 1; }
.block { border: 1px solid; border-radius: 8px; padding: 10px 14px 12px; display: flex; flex-direction: column; }
.block.human { background: var(--h-bg); border-color: var(--h-line); color: var(--h-ink); }
.block.agent { background: var(--a-bg); border-color: var(--a-line); color: var(--a-ink); }
.block.empty { border-style: dashed; border-width: 2px; }
.block header { display: flex; justify-content: space-between; gap: 8px; align-items: baseline; }
h3 { margin: 0; font-size: 16px; } .num { opacity: .7; margin-right: 4px; }
.badge { font-size: 11px; border: 1px solid currentColor; border-radius: 10px; padding: 1px 8px; background: var(--bg); white-space: nowrap; }
.body { color: var(--ink); } .body p { margin: 6px 0; } .body ul { margin: 6px 0; padding-left: 18px; }
.hint { color: var(--muted); font-style: italic; }
.state { margin: 6px 0 0; font-weight: 700; color: var(--warn); }
.block footer { margin-top: auto; padding-top: 6px; font-size: 11px; color: var(--muted); }
.newer { color: var(--warn); font-weight: 700; }
code { font-size: 12px; }
a { color: inherit; }
blockquote { margin: 6px 0; padding-left: 8px; border-left: 3px solid var(--rule); color: var(--muted); }
.tail { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin-top: 18px; }
.note { background: var(--n-bg); border: 1px solid var(--n-line); border-radius: 8px; padding: 10px 14px; }
.note h3 { font-size: 15px; }
.log { list-style: none; padding: 0; margin: 6px 0; } .log li { margin: 3px 0; }
.log time { color: var(--muted); font-variant-numeric: tabular-nums; margin-right: 6px; }
.blocks { font-size: 11px; border: 1px solid var(--rule); border-radius: 8px; padding: 0 6px; color: var(--muted); }
.legend { display: flex; gap: 20px; margin-top: 16px; font-size: 11.5px; flex-wrap: wrap; }
.sw { display: inline-block; width: 13px; height: 13px; border-radius: 3px; border: 1px solid; vertical-align: -2px; margin-right: 6px; }
.sw.human { background: var(--h-bg); border-color: var(--h-line); } .sw.agent { background: var(--a-bg); border-color: var(--a-line); }
.src { margin-left: auto; color: var(--muted); }
@media (max-width: 900px) { body { padding: 16px; } .grid, .tail { grid-template-columns: 1fr !important; }
  .cards { grid-template-rows: none !important; height: auto; } .cards > div { grid-row: auto !important; } }
@media print { @page { size: A3 landscape; margin: 10mm; } body { padding: 0; } .block { break-inside: avoid; } }
"""


def build(source, out, decisions_path, watch):
    canvas = parse_canvas(source.read_text(encoding="utf-8"))
    if not canvas["columns"]:
        sys.exit(f"No blocks found in {source}: expected '## Section' and '### N. Block 👤|🤖' headings.")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(canvas, parse_decisions(decisions_path), source, watch), encoding="utf-8")


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("canvas", type=pathlib.Path)
    p.add_argument("--out", type=pathlib.Path, default=pathlib.Path("build/canvas.html"))
    p.add_argument("--decisions", type=pathlib.Path,
                   help="decision log (default: DECISIONS.md next to the canvas, if it exists)")
    p.add_argument("--watch", action="store_true", help="re-render whenever the canvas or the log changes")
    a = p.parse_args()
    decisions = a.decisions or a.canvas.with_name("DECISIONS.md")
    build(a.canvas, a.out, decisions, a.watch)
    print(f"Wrote {a.out}", flush=True)
    if not a.watch:
        return
    print("Watching for changes (Ctrl+C to stop).", flush=True)
    mtimes = lambda: tuple(f.stat().st_mtime if f.exists() else 0 for f in (a.canvas, decisions))
    last = mtimes()
    try:
        while True:
            time.sleep(1)
            if (now := mtimes()) != last:
                last = now
                build(a.canvas, a.out, decisions, a.watch)
                print(f"Updated {a.out}", flush=True)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
