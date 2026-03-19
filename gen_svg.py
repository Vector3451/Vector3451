import random

orig_lines = [
    "\u2588\u2588\u2557   \u2588\u2588\u2557\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557 \u2588\u2588\u2588\u2588\u2588\u2588\u2557\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557 \u2588\u2588\u2588\u2588\u2588\u2588\u2557 \u2588\u2588\u2588\u2588\u2588\u2588\u2557 ",
    "\u2588\u2588\u2551   \u2588\u2588\u2551\u2588\u2588\u2554\u2550\u2550\u2550\u2550\u255d\u2588\u2588\u2554\u2550\u2550\u2550\u2550\u255d\u255a\u2550\u2550\u2588\u2588\u2554\u2550\u2550\u255d\u2588\u2588\u2554\u2550\u2550\u2550\u2588\u2588\u2557\u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2557",
    "\u2588\u2588\u2551   \u2588\u2588\u2551\u2588\u2588\u2588\u2588\u2588\u2557  \u2588\u2588\u2551        \u2588\u2588\u2551   \u2588\u2588\u2551   \u2588\u2588\u2551\u2588\u2588\u2588\u2588\u2588\u2588\u2554\u255d",
    "\u255a\u2588\u2588\u2557 \u2588\u2588\u2554\u255d\u2588\u2588\u2554\u2550\u2550\u255d  \u2588\u2588\u2551        \u2588\u2588\u2551   \u2588\u2588\u2551   \u2588\u2588\u2551\u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2557",
    " \u255a\u2588\u2588\u2588\u2588\u2554\u255d \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557\u255a\u2588\u2588\u2588\u2588\u2588\u2588\u2557   \u2588\u2588\u2551   \u255a\u2588\u2588\u2588\u2588\u2588\u2588\u2554\u255d\u2588\u2588\u2551  \u2588\u2588\u2551",
    "  \u255a\u2550\u2550\u2550\u255d  \u255a\u2550\u2550\u2550\u2550\u2550\u2550\u255d \u255a\u2550\u2550\u2550\u2550\u2550\u255d   \u255a\u2550\u255d    \u255a\u2550\u2550\u2550\u2550\u2550\u255d \u255a\u2550\u255d  \u255a\u2550\u255d"
]
width = max(len(l) for l in orig_lines)

def escape(s):
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def render_line(line, f):
    out = ""
    for x, char in enumerate(line.ljust(width, " ")):
        if char == "\u2588":
            dist = f - x
            if 0 <= dist <= 1: char = "\u2591"
            elif 2 <= dist <= 3: char = "\u2592"
            elif 4 <= dist <= 5: char = "\u2593"
        out += char
    return escape(out)

BASE_Y = 40
LINE_H = 20
FONT = "font-family:'Courier New',monospace;font-size:16px;white-space:pre;font-weight:bold;text-anchor:middle;"

def make_normal_frame(f):
    rows = []
    for y, line in enumerate(orig_lines):
        rendered = render_line(line, f)
        rows.append(f'    <text x="50%" y="{BASE_Y + y*LINE_H}" style="{FONT}fill:#00B4D8;">{rendered}</text>')
    return rows

def make_glitch_frame(f):
    """Visual glitch: applying slice rows into bands with horizontal offsets + random row shifts"""
    rows = []
    for y, line in enumerate(orig_lines):
        rendered = render_line(line, f)
        # Shift slightly using dx or just shift x="50% + rand"
        dx = random.randint(-15, 15)
        glitch_y = BASE_Y + y*LINE_H + random.choice([-3, 0, 0, 0, 3])
        colour = random.choice(["#00B4D8", "#00B4D8", "#00B4D8", "#ff003c", "#00e5ff"])
        
        # Optionally render a duplicate ghost slightly offset
        rows.append(f'    <text x="50%" dx="{dx + 5}" y="{glitch_y}" style="{FONT}fill:#ff003c;opacity:0.35;">{rendered}</text>')
        rows.append(f'    <text x="50%" dx="{dx}" y="{glitch_y}" style="{FONT}fill:{colour};">{rendered}</text>')
    return rows

frames = []
for f in range(width + 6):
    frames.append(make_normal_frame(f))
    if f % 12 == 0:
        frames.append(make_glitch_frame(f))
        frames.append(make_glitch_frame(f))

total = len(frames)
dur = total * 0.08

lines_out = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="800" height="200" viewBox="0 0 800 200">',
    '<style>',
    '.fr{opacity:0}',
]
for i in range(total):
    lines_out.append(f".f{i}{{animation:p {dur:.2f}s {i*0.08:.2f}s infinite step-end;}}")
pct = 1/total*100
lines_out += [
    f"@keyframes p{{0%{{opacity:1}}{pct:.3f}%{{opacity:0}}100%{{opacity:0}}}}",
    '</style>',
    '<rect width="100%" height="100%" fill="#0d1117" rx="8"/>',
]
for i, frame_rows in enumerate(frames):
    lines_out.append(f'<g class="fr f{i}">')
    lines_out += frame_rows
    lines_out.append('</g>')
lines_out.append('</svg>')

with open("animated_logo.svg","w",encoding="utf-8") as fh:
    fh.write("\n".join(lines_out))
print(f"Done: {total} frames, {dur:.2f}s")
