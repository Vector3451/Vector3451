import random, sys

orig_lines = [
    "\u2588\u2588\u2557   \u2588\u2588\u2557\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557 \u2588\u2588\u2588\u2588\u2588\u2588\u2557\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557 \u2588\u2588\u2588\u2588\u2588\u2588\u2557 \u2588\u2588\u2588\u2588\u2588\u2588\u2557 ",
    "\u2588\u2588\u2551   \u2588\u2588\u2551\u2588\u2588\u2554\u2550\u2550\u2550\u2550\u255d\u2588\u2588\u2554\u2550\u2550\u2550\u2550\u255d\u255a\u2550\u2550\u2588\u2588\u2554\u2550\u2550\u255d\u2588\u2588\u2554\u2550\u2550\u2550\u2588\u2588\u2557\u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2557",
    "\u2588\u2588\u2551   \u2588\u2588\u2551\u2588\u2588\u2588\u2588\u2588\u2557  \u2588\u2588\u2551        \u2588\u2588\u2551   \u2588\u2588\u2551   \u2588\u2588\u2551\u2588\u2588\u2588\u2588\u2588\u2588\u2554\u255d",
    "\u255a\u2588\u2588\u2557 \u2588\u2588\u2554\u255d\u2588\u2588\u2554\u2550\u2550\u255d  \u2588\u2588\u2551        \u2588\u2588\u2551   \u2588\u2588\u2551   \u2588\u2588\u2551\u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2557",
    " \u255a\u2588\u2588\u2588\u2588\u2554\u255d \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557\u255a\u2588\u2588\u2588\u2588\u2588\u2588\u2557   \u2588\u2588\u2551   \u255a\u2588\u2588\u2588\u2588\u2588\u2588\u2554\u255d\u2588\u2588\u2551  \u2588\u2588\u2551",
    "  \u255a\u2550\u2550\u2550\u255d  \u255a\u2550\u2550\u2550\u2550\u2550\u2550\u255d \u255a\u2550\u2550\u2550\u2550\u2550\u255d   \u255a\u2550\u255d    \u255a\u2550\u2550\u2550\u2550\u2550\u255d \u255a\u2550\u255d  \u255a\u2550\u255d"
]

width = max(len(l) for l in orig_lines)

def build_frame(f, glitch=False):
    rows = []
    for y, line in enumerate(orig_lines):
        new_line = ""
        for x, char in enumerate(line.ljust(width, " ")):
            if char == "\u2588":
                dist = f - x
                if 0 <= dist <= 1: new_char = "\u2591"
                elif 2 <= dist <= 3: new_char = "\u2592"
                elif 4 <= dist <= 5: new_char = "\u2593"
                else: new_char = "\u2588"
                if glitch and random.random() < 0.08:
                    new_char = random.choice(["\u2591","\u2592","\u2593"," "])
            else:
                new_char = char
            new_line += new_char
        new_line = new_line.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
        fill = "#ff003c" if glitch else "#00B4D8"
        rows.append(f'    <text x="155" y="{40+y*20}" style="font-family:\'Courier New\',monospace;font-size:16px;fill:{fill};white-space:pre;font-weight:bold;">{new_line}</text>')
    return rows

frames = []
for f in range(width + 6):
    frames.append(build_frame(f, False))
    # insert a glitch ghost every ~15 frames
    if f % 15 == 0:
        frames.append(build_frame(f, True))

total = len(frames)
dur = total * 0.08

lines = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="800" height="200" viewBox="0 0 800 200">',
    '  <style>',
    '    .frame{opacity:0}',
]
for i in range(total):
    lines.append(f"    .f{i}{{animation:pulse {dur:.2f}s {i*0.08:.2f}s infinite step-end;}}")
lines += [
    '    @keyframes pulse{0%{opacity:1}' + f'{(1/total*100):.3f}' + '%{opacity:0}100%{opacity:0}}',
    '  </style>',
    '  <rect width="100%" height="100%" fill="#0d1117" rx="8"/>',
]
for i, frame_rows in enumerate(frames):
    lines.append(f'  <g class="frame f{i}">')
    lines += frame_rows
    lines.append('  </g>')
lines.append('</svg>')

with open("animated_logo.svg","w",encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"Done: {total} frames, dur={dur:.2f}s")
