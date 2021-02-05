---
description: Unikraft is a Linux Foundation project able to build extremely efficient
  and secure software stacks/unikernels. By tailoring the operating system, libraries
  and tools to the particular needs of each application, it vastly reduces virtual
  machine and container image sizes to a few KBs, drastically cutting down the software
  stack's attack surface. Our evaluation using off-the-shelf popular applications
  such as Nginx, SQLite, and Redis shows that running such applications on Unikraft
  results in a 30%-50% performance improvement compared to Linux guests. In addition,
  Unikraft images for these apps are around 1MB, require less than 10MB of RAM to
  run, and boot in around 1ms on top of the VMM time (total boot time 2ms-70ms). Finally,
  we are hard at work integrating Unikraft into standard frameworks such as Kubernetes
  and Cloud Foundry.
layout: stand
logo: stands/unikraft/logo.png
new_this_year: "Since our last presentation at FOSDEM2020, in addition to growing\
  \ the community, we have added a large amount of features to Unikraft:\r\n\r\n*\
  \ Security features, including stack protection, ASAN, Intel MPK, etc.\r\n* Increasing\
  \ POSIX support (140+ syscalls and counting), including support for standard applications\
  \ (e.g., nginx, SQLite, Redis, etc.)\r\n* Native support for many programming languages\
  \ and language environments: C++, Python/Micropython, Go, Lua, Web Assembly (WAMR),\
  \ JavaScript (Duktape), Ruby and Rust (ongoing).\r\n* Network performance optimizations\
  \ for KVM\r\n* Support for networking and performance optimizations for Xen\r\n\
  * ARM64 bare metal support for the Raspberry Pi 3 and the Xilinx Ultra96-v2 boards\r\
  \n* Page table support\r\n* Initial support for Amazon Firecracker\r\n* Cloud-based\
  \ deployments (GCP, AWS, Digital Ocean)\r\n* Improvements to the ARM64 platform,\
  \ including virtio and multi-thread support\r\n* Basic musl support\r\n\r\nAnd lots\
  \ of other features and bug fixes."
showcase: If you run significant amount of services on public cloud infrastructure,
  you should come to our stand to find out how Unikraft can help you seamlessly debloat
  your deployments; for example, in recent experiments on AWS we have been able to
  cut costs by half when running NGINX compared to a Linux image. If you come from
  the automotive industry, Unikraft can act as a minimal guest that can provide POSIX-like
  functionality while providing a relatively cheap certification path. And if you
  work on IoT or edge cloud deployments, Unikraft can even run bare metal on ARM devices,
  providing substantial efficiency on such hardware-constrained devices.
themes:
- Operating systems
title: Unikraft
website: http://www.unikraft.org/
show_on_overview: true
chatroom: unikraft
draft: true
---