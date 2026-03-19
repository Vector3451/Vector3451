import sys

orig_lines = [
    "\u2588\u2588\u2557   \u2588\u2588\u2557\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557 \u2588\u2588\u2588\u2588\u2588\u2588\u2557\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557 \u2588\u2588\u2588\u2588\u2588\u2588\u2557 \u2588\u2588\u2588\u2588\u2588\u2588\u2557 ",
    "\u2588\u2588\u2551   \u2588\u2588\u2551\u2588\u2588\u2554\u2550\u2550\u2550\u2550\u255D\u2588\u2588\u2554\u2550\u2550\u2550\u2550\u255D\u255A\u2550\u2550\u2588\u2588\u2554\u2550\u2550\u255D\u2588\u2588\u2554\u2550\u2550\u2550\u2588\u2588\u2557\u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2557",
    "\u2588\u2588\u2551   \u2588\u2588\u2551\u2588\u2588\u2588\u2588\u2588\u2557  \u2588\u2588\u2551        \u2588\u2588\u2551   \u2588\u2588\u2551   \u2588\u2588\u2551\u2588\u2588\u2588\u2588\u2588\u2588\u2554\u255D",
    "\u255A\u2588\u2588\u2557 \u2588\u2588\u2554\u255D\u2588\u2588\u2554\u2550\u2550\u255D  \u2588\u2588\u2551        \u2588\u2588\u2551   \u2588\u2588\u2551   \u2588\u2588\u2551\u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2557",
    " \u255A\u2588\u2588\u2588\u2588\u2554\u255D \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557\u255A\u2588\u2588\u2588\u2588\u2588\u2588\u2557   \u2588\u2588\u2551   \u255A\u2588\u2588\u2588\u2588\u2588\u2588\u2554\u255D\u2588\u2588\u2551  \u2588\u2588\u2551",
    "  \u255A\u2550\u2550\u2550\u255D  \u255A\u2550\u2550\u2550\u2550\u2550\u2550\u255D \u255A\u2550\u2550\u2550\u2550\u2550\u255D   \u255A\u2550\u255D    \u255A\u2550\u2550\u2550\u2550\u2550\u255D \u255A\u2550\u255D  \u255A\u2550\u255D"
]

width = max(len(l) for l in orig_lines)
height = len(orig_lines)
frames_count = width + 6

svg_content = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="800" height="200" viewBox="0 0 800 200">',
    '  <style>',
    '    .txt { font-family: "Courier New", Courier, monospace; font-size: 16px; fill: #00B4D8; white-space: pre; font-weight: bold; }',
    '    .frame { opacity: 0; animation: pulse ' + str(frames_count * 0.1) + 's infinite step-end; }',
    '    .glitch { animation: glitch_anim 3s infinite step-none; }',
    '    @keyframes glitch_anim {',
    '      0% { transform: translate(0,0); }',
    '      92% { transform: translate(0,0); fill: #00B4D8; opacity: 1; }',
    '      93% { transform: translate(-3px, 1px) skewX(5deg); fill: #ff003c; opacity: 0.8; }',
    '      94% { transform: translate(3px, -2px) skewX(-5deg); fill: #00e5ff; opacity: 0.8; }',
    '      95% { transform: translate(0,0); fill: #00B4D8; opacity: 1; }',
    '      100% { transform: translate(0,0); }',
    '    }'
]

for f in range(frames_count):
    percent = (f / frames_count) * 100
    svg_content.append(f"    .f{f} {{ animation-delay: {f * 0.1:.2f}s; }}")

svg_content.append('    @keyframes pulse {')
svg_content.append(f'      0% {{ opacity: 1; }}')
frame_pct = (1.0 / frames_count) * 100
svg_content.append(f'      {frame_pct:.3f}% {{ opacity: 0; }}')
svg_content.append('      100% { opacity: 0; }')
svg_content.append('    }')
svg_content.append('  </style>')
svg_content.append('  <rect width="100%" height="100%" fill="#0d1117" rx="8" />')

for f in range(frames_count):
    svg_content.append(f'  <g class="frame f{f}">')
    for y, line in enumerate(orig_lines):
        new_line = ""
        for x, char in enumerate(line.ljust(width, " ")):
            if char == "\u2588":
                dist = f - x
                if 0 <= dist <= 1: new_char = "\u2591" # light
                elif 2 <= dist <= 3: new_char = "\u2592" # med
                elif 4 <= dist <= 5: new_char = "\u2593" # dark
                else: new_char = "\u2588"
                new_line += new_char
            else:
                new_line += char
        
        # XML escape
        new_line = new_line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        
        y_pos = 40 + y * 20
        svg_content.append(f'    <text x="155" y="{y_pos}" class="txt glitch">{new_line}</text>')
    svg_content.append('  </g>')

svg_content.append('</svg>')

with open("Vector3451_profile/animated_logo.svg", "w", encoding="utf-8") as file:
    file.write("\n".join(svg_content))

print("SVG Generated.")
