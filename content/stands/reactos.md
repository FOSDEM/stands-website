---
description: |
  ReactOS is a modern open source operating system based on the Windows XP/2003 design.
  It was written from scratch with the goal of full compatibility with Windows applications and drivers, as well as a similar user interface so that most users can find their way around immediately.
  The source code for the entire system is freely available under either the GNU GPL, BSD or similar license.<br>
  <br>
  ReactOS's unique ability to use applications and drivers developed for Windows makes it the open source operating system with the broadest hardware and software support.
  In addition, it is based on the design of the NT kernel, which makes it scalable, portable and performant.
  In addition to the well-known Win32 support, this also enables other subsystems, for example POSIX, or the DOS/Win16 VDM, which is already under development.
layout: stand
logo: stands/reactos/logo.png
new_this_year: |
  <p>A lot of work has been done in both kernel and user mode parts of ReactOS.</p>

  <p>User mode changes:
  <ul>
    <li>Filesystem notifications in shell</li>
    <li>Many small UI polishing changes, like autocomplete text fields, "size on disk" label for file properties dialog</li>
    <li>More work towards forward compatibility with recent Windows apps</li>
    <li>ReactOS Applications manager (Rapps) enchancement (one of our GSoC projects):<br>
    Support for displaying screenshots, visual changes, command-line scripting improvements</li>
  </ul>
  </p>

  <p>The most notable kernel changes are:
  <ul>
    <li>new storage stack, derived from open source Microsoft drivers.<br>
    Offers compatibility with vendor-provided storage drivers, and other software,<br>
    GPT partitions support, SSD special commands, blu-ray drives and more</li>
    <li>Compatibility improvements in Cache Controller subsystem and Memory Manager.<br>
    Support for filesystem drivers for Windows improved a lot,<br>
    now "ntfs.sys" driver from Windows almost works and FAT driver works without issues</li>
    <li>Plug and Play manager improvements, for better 3rd party driver support</li>
    <li>amd64 support progress, now it boots to the desktop</li>
    <li>original Xbox port improved, and NEC PC-98 port started</li>
  </ul>
  </p>
showcase: |
  <p>We are a one of a kind project aiming to recreate Windows&nbsp;NT from ground up, cleanly and legally.
  All code is freely available for anyone to tinker with.</p>
  <p>We will show on our stand what was and is possible with our quite limited manpower
  and give a little insight to what can happen when a few developers are getting paid for a few months,
  how much the whole project can improve just by support on paid work base for a short time period.</p>
  <p>Of course we can and will try to answer all questions our visitors have regarding the project,
  the current status and what we will expect to happen soon.
  We have still some big improvements left to come soon and plan to show some of these live in a preview.</p>
  <p>We will show working real hardware, real Windows applications running and all with real Windows 3rd party closed source drivers being used.
  All on a FOSS Windows like system.</p>
themes:
- Operating systems
title: ReactOS
website: https://reactos.org/
show_on_overview: true
chatroom: reactos
---