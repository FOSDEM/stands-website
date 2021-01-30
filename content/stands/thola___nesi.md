---
description: "Thola is a new open source tool for reading, monitoring and provisioning\
  \ network devices written in Go. \r\n\r\nThis stand will inform about the current\
  \ state of development as well as planned features, including reading out inventory,\
  \ configuring network devices, support for other monitoring systems like prometheus\
  \ and many more.\r\n\r\nIt serves as a unified interface for communication with\
  \ network devices and features a check mode which complies with the monitoring plugins\
  \ development guidelines and is therefore compatible with Nagios, Icinga, Zabbix,\
  \ Checkmk, etc.\r\n\r\nWith the NESi software we aim at simulating certain points\
  \ of a network. \r\n\r\nAt the Moment we are able to simulate DSLAMs (Digital Subscriber\
  \ Line Multiplexer) of various vendors including Alcatel, Huawei and KeyMile to\
  \ name the most popular.\r\n\r\nThe software itself can simulate the vendors OS\
  \ running on the network-device and allows the user to configure the amount of network\
  \ cards, the number of ports on said cards and connected CPEs (Customer Premises\
  \ Equipment). \r\n\r\nThe idea of the software originated from Ilya Etingof, the\
  \ creator of snmpsim. A python based software to simulate snmp calls to a network-device.\
  \ In a future release of NESi we are planning on integrating snmpsim into our framework\
  \ as well."
layout: stand
logo: stands/thola___nesi/logo.png
new_this_year: "This would be the first time we have a stand on FOSDEM. Thola and\
  \ NESi are quite new projects, we would like to introduce them.\r\nThola\r\n- support\
  \ for different network device types like switches, routers, WDM, directional radio,\
  \ UPS, DSLAM/OLT,... including type specific requests and checks\r\n- an easy way\
  \ for adding support for additional devices by YAML configuration files\r\n- support\
  \ for different network protocols like SNMP, HTTP(S), telnet/ssh (coming soon) and\
  \ more\r\n- a check plugin mode compatible with Icinga, Nagios, Zabbix, Checkmk,\
  \ ...\r\n- a REST API mode\r\n- low resource needs\r\n\r\nNESi (Network Equipment\
  \ Simulator)\r\nSupported Vendors\r\n- Alcatel  (nearly feature complete)\r\n- Huawei\
  \   (nearly feature complete)\r\n- Keymile  (work in progress)\r\n\r\nSupported\
  \ network components\r\n- Subracks\r\n- Cards\r\n- Ports\r\n- ONTs\r\n- CPEs\r\n\
  - Vlans\r\n\r\nUpcoming features this year in both projects:\r\nThola should be\
  \ easy to install and implement in the most known existing monitoring systems.\r\
  \nNESi should cover nearly all big vendors to simulate the CLI and snmpsim by Ilya\
  \ Etingof should be integrated in NESi."
showcase: "People who love everything about network monitoring and provisioning.\r\
  \nPeople who got large networks and are interested in how to manage them with one\
  \ unified interface.\r\nPeople who love the programming language GO.\r\nPeople who\
  \ love to contribute in new OS projects.\r\nPeople who are searching for a smart\
  \ monitoring solution, based on an open source project.\r\nPeople who are interested\
  \ to see how network devices can be handled easy with an unified interface.\r\n\
  People who may got trouble with vendor specific snmp requests and responses.\r\n\
  People who would like to be part of a new, revolutionary, OS project.\r\nPeople\
  \ who love to simulate a large environment with many different network devices.\r\
  \nPeople who love to simulate a command line interface as well as a snmp interface\
  \ of a network device."
themes:
- System administration
title: Thola / NESi
website: https://thola.io
show_on_overview: true
chatroom: thola
draft: true
---