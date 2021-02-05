---
description: |
  Box86 allows to run 32bits x86 applications on ARM devices.

  Playing linux games, like WorldOfGoo, FTL or Unreal Tournament 2004 on a RaspberryPI 4 or other SBC, becomes possible with Box86. Using Wine is also supported, opening a lot more possibilities and enhancing the compatibility of ARM board.
  
  You are not limited on games with box86, and you can use it to run Zoom linux client, or setup a Teamspeak or Game Server.
  
  Box86 combine a fast Dynarec that converts on the fly x86 code to ARM code, with native library wrapping to avoid emulating frequently used functions and to be able to use box86 super easily: no need for a full x86 chroot system, most used libraries are the native versions.
layout: stand
show_on_overview: true
logo: stands/box86/logo.png
new_this_year: |
  <p>Box86 is targeted towards 32bits. While compatibility and speed can be improved, the support of 16bits code (for Wine) is probably the last missing feature for box86.</p>
  <p>After that, Box64 will be targeted toward 64bits apps. It will be a different application, and will allow similar principles with native use of ARM64 native libs directly on x86_64 linux apps.</p>
showcase: <p>Discover new possibilties for your RaspberryPI 4 and all other ARM SBC with
  Box86. Playing FTL or Into the Breach, Unreal Tournament 99 or 2004, or racing a
  few laps on Flatout (to name just a few) becomes possible on a small SBC.</p>
themes:
- Gaming
title: Box86
website: https://ptitseb.github.io/box86/
chatroom: box86
---
