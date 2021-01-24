---
description: |
  OpenEmbedded provides a build environment for cross-compilation, packaging
   and creation of images for Linux-based embedded systems.
  
  OpenEmbedded supports
   building a wide variety of software and includes support for various popular programming
   languages such as C, C++, Perl, Python, Java, C# (Mono), Rust, Go and more.
   
  Popular projects that use OpenEmbedded at their core include the Yocto Project,
   Gumstix, WebOS, Beagleboard/Pandaboard, etc. We also support building images for
   common single board computers such as the Raspberry Pi.
layout: stand
logo: stands/openembedded/logo.png
new_this_year: |
  <p>Since FOSDEM 2020, the OpenEmbedded project has made two major releases
    on our usual 6-month schedule, "dunfell" in April and "gatesgarth" in November,
    along with several minor maintenance releases to fix bugs and security issues
    in upstream projects. Working with Yocto Project, the "dunfell" release is our
    first Long Term Support (LTS) release which will be maintained for at least 2
    years from the initial release date. The "dunfell" release included major improvements
    to reproducible builds, the hash equivalence server and other key project features.
    This was also our first release to be entirely free of obsolete Python 2 dependencies
    within the core metadata (although Python 2 support continues to be available
    via the meta-python2 layer). Our most recent release includes support for GCC
    10, Linux 5.8, glibc 2.32 as well as around 245 other recipe upgrades and represents
    the work of over 170 contributors to the project. Support for new programming
    languages such as Rust and new target architectures such as RISCV continues to
    improve.</p>
  <p>The project is currently working towards the next release codenamed
    "hardknott" which is scheduled for April 2021. Further improvements are expected
    to the build reproducibility, autobuilder, hash equivalency service and security
    processes. We're also working on bringing full support for Rust into the core
    metadata. A new locked sstate feature is being planned which if successfully integrated
    will allow improvements to the extensible SDK and enable better use of sstate
    mirrors to accelerate builds. The regular process of upgrading recipes continues
    as ever, with support for the new Linux 5.10 LTS release expected to land in our
    master branch before FOSDEM 2021.</p>
showcase: |
  <p>The OpenEmbedded project allows you to build a fully customised Embedded
    Linux distribution for a wide variety of target hardware and applications. Each
    package is cross-compiled from source with many configuration options exposed
    allowing you to perform any level of fine tuning you desire. As well as producing
    ready-to-use images which can be copied to SD card, flash memory or other appropriate
    storage and booted on the target device, with OpenEmbedded you can maintain custom
    package feeds and other artifacts enabling direct or over-the-air (OTA) update
    of the software on your device after installation. OpenEmbedded also supports
    building Docker-compatible container images with license compliance tooling and
    reproducibility which can't be found when creating images via a Dockerfile.</p>
  <p>Our virtual stand this year will showcase some of the third-party hardware which
    is supported by OpenEmbedded as well as some of the applications you can build
    and deploy. We'll show you how to get started with the project and where to find
    our community online. Various developers and users within our community will be
    hosting the stand at different times so feel free to drop by and say hello!</p>
themes:
- IoT
title: OpenEmbedded
website: https://www.openembedded.org/wiki/Main_Page
show_on_overview: true
---