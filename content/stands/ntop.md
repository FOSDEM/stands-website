---
description: ntop started as an opensource project in 1998 whose goal was to create
  a simple yet effective web-based traffic monitoring platform. Many things have changed
  since then, including the nature of the traffic being analyzed, operating systems
  being run, and the way users interact with technologies. During this time, ntop
  has evolved into a fully-fledged research company with many opensource projects
  whose main spirit is still the original one, namely, to innovate network monitoring
  using commodity hardware and freely available operating systems.
layout: stand
logo: stands/ntop/logo.png
new_this_year: "Since our last FOSDEM, ntopng has evolved along key dimensions:\r\n\
  \r\n- Input data. ntopng features the ability to receive and combine data from multiple,\
  \ heterogeneous sources. These sources include, but are not limited to, raw traffic\
  \ data, NetFlow and sFlow, firewalls and intrusion detection and prevention systems\
  \ such as Suricata.\r\n- Output data. Insights and intelligence data can be delivered\
  \ to multiple downstream recipients, including big-data stores (Elasticsearch),\
  \ messaging systems (Discord, Slack), email, and more.\r\n- External consumers.\
  \ A simple REST API exposes data to external consumers. This has paved the way for\
  \ the integration with Check MK, another popular opensource monitoring tool.\r\n\
  - Extensibility. Developers and community contributors can extend ntopng functionalities\
  \ by means of simple Lua scripts, that gets executed by ntopng.\r\n- Encrypted traffic\
  \ analysis. Encrypted TLS traffic is performed to provide insights into the nature\
  \ and security of monitored encrypted communications.\r\n- Behavior analyses. Heuristics\
  \ aim at detecting changes in normal and periodic traffic to detect new and possibly\
  \ suspicious host behaviors.\r\n\r\nFor this year, we expect ntopng to keep growing\
  \ and becoming more open to other opensource projects. Strong focus will be kept\
  \ on the security aspects of network monitoring, including behavioral and encrypted\
  \ traffic analyses. Finally, small agents are being built under the hood to be used\
  \ in combination with ntopng and to leverage its intelligence to block suspicious\
  \ traffic and prevent malicious activities to disrupt the whole network."
showcase: "ntop features many opensource projects freely available on GitHub. This\
  \ stand wants to showcase one of the most popular opensource software developed\
  \ by ntop, namely, ntopng. ntopng is a web-based traffic monitoring software that\
  \ combines and correlates raw traffic data with other information to effectively\
  \ provide network intelligence an actionable insights.\r\nntopng can be used in\
  \ heterogeneous environments, ranging from homes and small offices, to large distributed\
  \ enterprise and research networks. Just to give an example, a real-world use case\
  \ of ntopng to monitor a large research network was presented at FOSDEM 2020.\r\n\
  ntopng integrates the opensource Deep Packet Inspection library nDPI to inspect\
  \ the whole protocol stack, up to the layer-7. This allows ntopng to provide intelligence\
  \ and insights both on traditional network metrics as well as on security-specific\
  \ metrics such as indicators of compromise.\r\nIf you visit our stand, you will\
  \ have to opportunity to see quick demonstrations of ntopng in action and learn\
  \ how to deploy it."
themes:
- World wide web
title: ntop
website: https://www.ntop.org/
show_on_overview: true
---