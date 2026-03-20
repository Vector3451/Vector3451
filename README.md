<!-- HEADER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:00b4d8,100:0d1117&height=80&section=header"/>
<div align="center">
<img src="animated_logo.svg?v=6" width="100%" alt="Vector3451 Animated Glitch Logo"/>

[![Visitors](https://komarev.com/ghpvc/?username=Vector3451&style=flat-square&color=00B4D8&labelColor=0d1117&label=VISITORS)](https://github.com/Vector3451)
&nbsp;
[![Followers](https://img.shields.io/github/followers/Vector3451?style=flat-square&color=00B4D8&labelColor=0d1117&label=FOLLOWERS&logo=github)](https://github.com/Vector3451)
&nbsp;
[![Stars](https://img.shields.io/github/stars/Vector3451?style=flat-square&color=00B4D8&labelColor=0d1117&label=STARS&logo=github)](https://github.com/Vector3451)
</div>

---

<!-- TERMINAL BREACH CTF -->
<div align="center">

```
>_ CTF_ENGINE  ···  breach.log
```

*Infiltrate the system. Find the 3 hidden flags to prove your rank.*<br/>

</div>

<br/>

<div align="left">

<details open>
<summary><code>🖤️ [remote@Vector3451] ~$ ./initialize_breach.sh</code></summary>

```yaml
STATUS: "SECURE_SHELL_OPEN"
MISSION: "Locate 3 hidden flags embedded in this system"
RULES:
  - No flag will simply be handed to you
  - You must decode, inspect, and think
  - Use: browser devtools, base64 decoders, rot13 tools
```
</details>

<details>
<summary><code>💻 LEVEL 1 — [remote@Vector3451] ~$ ls /proc/net/intercept</code></summary>

```diff
+ [SYS] Scanned 256 ports. One service is leaking.
+ [SYS] The port number itself is the key offset.
! Decode this ROT13 string to find it:
  synt{1_cbeg_fpna_pbzcyrgrq}
# HINT: Use rot13.com or any ROT13 decoder. The result IS your flag.
```
</details>

<details>
<summary><code>💻 LEVEL 2 — [remote@Vector3451] ~$ strings /dev/null | grep HIDDEN</code></summary>

```diff
- [ICE] FIREWALL ACTIVE. PAYLOAD REJECTED.
! [SYS] Binary fragments intercepted from memory:
  01100110 01101100 01100001 01100111 01111011 00110010
  01011111 01100110 01101001 01110010 01100101 01110111
  01100001 01101100 01101100 01011111 01100100 01110010
  01101111 01110000 01110000 01100101 01100100 01111101
# HINT: Convert each 8-bit binary group to ASCII. The full string is your flag.
```
</details>

<details>
<summary><code>💻 LEVEL 3 — [remote@Vector3451] ~$ read_memory --hex --offset 0xDEAD</code></summary>

```diff
- [KERNEL] MEMORY READ FAILED. SEGMENT PROTECTED.
! [SYS] One commit in this repository carries the final flag in its message.
! [SYS] Navigate to the commit history: github.com/Vector3451/Vector3451/commits
# HINT: Look for a commit titled with a hex string. The flag is hidden in the message body.
```

```yaml
MISSION: "If you found all 3 flags, congratulations. You are in."
REWARD: "Click the badge below to claim your master access token."
```

<details>
<summary><code>🏆 [remote@Vector3451] ~$ view_flag_status</code></summary>

<br/>

<table align="center">
  <tr>
    <td align="center" width="200">
      <img src="https://img.shields.io/badge/LEVEL_01-ROT__13-00B4D8?style=for-the-badge" /><br/>
      <code>[ LOCKED ]</code><br/>
      🚩
    </td>
    <td align="center" width="200">
      <img src="https://img.shields.io/badge/LEVEL_02-BINARY-00B4D8?style=for-the-badge" /><br/>
      <code>[ LOCKED ]</code><br/>
      🚩
    </td>
    <td align="center" width="200">
      <img src="https://img.shields.io/badge/LEVEL_03-GIT__HISTORY-00B4D8?style=for-the-badge" /><br/>
      <code>[ LOCKED ]</code><br/>
      🚩
    </td>
  </tr>
</table>

</details>

<a href="https://vector3451.github.io/Vector3451/flag_tracker.html"><img src="https://img.shields.io/badge/⚑_LAUNCH_TRACKER-INTERACT_IN_BROWSER-00B4D8?style=for-the-badge&logo=hackaday&logoColor=white" alt="Flag Tracker"/></a>
&nbsp;
<a href="https://github.com/Vector3451"><img src="https://img.shields.io/badge/ACCESS_GRANTED-SYSTEM_MASTER-00B4D8?style=for-the-badge&logo=hackthebox&logoColor=white" alt="Access Granted Reward"/></a>
</details>

<details>
<summary><code>📡 [remote@Vector3451] ~$ decode_hints --all</code></summary>

```yaml
LEVEL_1:
  tool: "rot13.com"
  input: "synt{1_cbeg_fpna_pbzcyrgrq}"
  action: "Paste the string, copy the output"

LEVEL_2:
  tool: "Any binary-to-text converter (e.g. rapidtables.com/convert/number/binary-to-ascii.html)"
  input: "The binary groups above"
  action: "Convert each 8-bit block to its ASCII character"

LEVEL_3:
  tool: "GitHub commit history"
  url: "github.com/Vector3451/Vector3451/commits/main"
  action: "Find the commit with a hex title. The flag is in its body."
```
</details>

</div>

---

<!-- AUDIO SEQUENCER -->
<div align="center">

```
>_ MUSIC SEQUENCER TERMINAL  ···  vector3451.wav
```

*Access the interactive 16-step 8-track Web Audio API synthesizer directly in your browser. Compose loop architectures, trigger drum synthesis, and manipulate frequency data.*

</div>

<!-- Inline sequencer embed via GitHub Pages -->
<div align="center">

<details open>
<summary><code>🎵 [remote@Vector3451] ~$ ./launch_sequencer.sh</code></summary>

<br/>

[![Sequencer Preview](https://readme-typing-svg.demolab.com?font=Share+Tech+Mono&size=14&duration=4000&pause=500&color=00ffea&center=true&vCenter=true&width=700&lines=TRACK_01+|+██++░░++░░++░░++██++░░++░░++░░++██++░░++░░++░░++██++░░++░░++░░;TRACK_02+|+░░++░░++░░++░░++██++░░++░░++░░++░░++░░++░░++░░++██++░░++░░++░░;TRACK_03+|+░░++░░++██++░░++░░++░░++██++░░++░░++░░++██++░░++░░++░░++██++░░;TRACK_04+|+░░++░░++░░++░░++░░++░░++░░++░░++░░++░░++░░++░░++░░++░░++░░++██;TRACK_05+|+░░++██++░░++░░++░░++██++░░++░░++░░++██++░░++░░++░░++██++░░++░░;TRACK_06+|+░░++░░++░░++██++░░++░░++░░++██++░░++░░++░░++██++░░++░░++░░++██;TRACK_07+|+░░++░░++░░++░░++░░++░░++██++░░++░░++░░++░░++░░++░░++░░++██++░░;TRACK_08+|+░░++░░++░░++░░++░░++░░++░░++░░++██++░░++░░++░░++░░++░░++░░++░░)](https://vector3451.github.io/Vector3451/sequencer.html)

<br/>

<a href="https://vector3451.github.io/Vector3451/sequencer.html">
  <img src="https://img.shields.io/badge/▶_LAUNCH_SEQUENCER-OPEN_IN_BROWSER-00B4D8?style=for-the-badge&logo=musicbrainz&logoColor=white" alt="Launch Sequencer"/>
</a>

> **🎹 Embedded Controls** — The sequencer interface runs entirely in your browser via GitHub Pages.  
> *8 tracks (Kick, Snare, Hihat, Clap, Bass, Lead, Pad, FX) spanning 16 synthesis steps.*

</details>

</div>

---

<!-- GITHUB METRICS -->
<div align="center">

```
>_ DIAGNOSTIC REPORT  ···  github.com/Vector3451
```

<img src="https://github-readme-stats.vercel.app/api?username=Vector3451&show_icons=true&theme=github_dark&hide_border=true&bg_color=0D1117&title_color=00B4D8&icon_color=00B4D8&text_color=C9D1D9&border_radius=4" height="160"/>
&nbsp;
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Vector3451&layout=compact&theme=github_dark&hide_border=true&bg_color=0D1117&title_color=00B4D8&text_color=C9D1D9&border_radius=4" height="160"/>

<img src="https://streak-stats.demolab.com?user=Vector3451&theme=github-dark-blue&hide_border=true&background=0D1117&ring=00B4D8&fire=00B4D8&currStreakLabel=00B4D8&sideLabels=9FB3C8&dates=C9D1D9&border_radius=4" width="60%"/>

</div>

---

<!-- LEETCODE -->
<div align="center">

```
>_ LEETCODE TERMINAL  ···  Vinay_Vijay_2.bin
```

<img src="https://leetcard.jacoblin.cool/Vinay_Vijay_2?theme=dark&font=Fira%20Code&ext=heatmap&border=0&radius=4&width=500&colors=0d1117,161b22,00B4D8,00B4D8,c9d1d9,00B4D8,ff7b72,ffa657,00B4D8" alt="LeetCode Stats"/>
</div>



<!-- FOOTER -->
<div align="center">


<img src="https://readme-typing-svg.demolab.com?font=Share+Tech+Mono&size=13&duration=3000&pause=1200&color=00B4D8&center=true&vCenter=true&width=480&lines=%24+shutdown+--graceful+--save+progress;Saving+state...+[OK];Committing+to+main...+[OK];Session+logged.+See+you+tomorrow."/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:00b4d8,100:0d1117&height=80&section=footer"/>
</div>
