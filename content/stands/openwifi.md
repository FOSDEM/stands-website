---
description: "openwifi: opensource WiFi chip!\r\n\r\nFeatures:\r\n802.11a/g/n\r\n\
  20MHz bandwidth; 70 MHz to 6 GHz frequency range\r\nMode tested: Ad-hoc; Station;\
  \ AP, Monitor\r\nDCF (CSMA/CA) low MAC layer in FPGA (10us SIFS is achieved)\r\n\
  Configurable channel access priority parameters:\r\n    duration of RTS/CTS, CTS-to-self\r\
  \n    SIFS/DIFS/xIFS/slot-time/CW/etc\r\nTime slicing based on MAC address\r\nEasy\
  \ to change bandwidth and frequency:\r\n    2MHz for 802.11ah in sub-GHz\r\n   \
  \ 10MHz for 802.11p/vehicle in 5.9GHz\r\nCSI (Channel State Information, freq offset,\
  \ equalizer to computer)\r\nIQ capture (real-time AGC, RSSI, IQ sample to computer)\r\
  \nOn roadmap: 802.11ax"
layout: stand
logo: stands/openwifi/logo.png
new_this_year: |
  <p>We have updates across our projects since FOSDEM'20:</p>
  <ul>
    <li>802.11n (WiFi4)!</li>
    <li>Port the design from a single type of FPGA dev board to 6 types of boards! From high end (as expensive as 3600USD) to low end (900USD).</li>
    <li>Low latency ping RTT (Round Trip Time): 200~300us.</li>
    <li>Essential improvement on stability, 802.11 compatibility and performance cross FPGA and Linux driver.</li>
    <li>Increase the FPGA packet queue from 2 to 4, meet the Linux mac80211 requirement/assumption about QoS/Priority-strategy better.</li>
    <li>Channel estimation and frequency offset compensation bug fix on the OFDM receiver. Better reception performance.</li>
    <li>CSI (Channel State Information) interface from FPGA to Linux. And it doesn't affect normal WiFi communication.</li>
    <li>IQ sample interface from FPGA to Linux. And it doesn't affect normal WiFi communication.</li>
    <li>Open the idea to Low cost SDR openwifi dongle (+/-200USD) and real chip tape out!</li>
  </ul>
showcase: "All of those opensource hardware projects are focusing on the CPU side:\r\
  \nRISC-V, all kinds of open CPU cores, Raspberry PI, xxxx PI, PINE64, openWRT, AI/machine-learning\
  \ accelerators.\r\nHowever the radio connectivity part of those opensource hardware\
  \ boards are still from black-box silicon (commercial chips, like WiFi chips from\
  \ big companies).\r\nOpenwifi project, which was announced in the FOSDEM'20, is\
  \ the first attempt to build an opensource chip in the radio connectivity domain!\r\
  \nNow we have tested the design on the FPGA development board (SDR -- Software Defined\
  \ Radio), and it works well in the real world scenario. Meanwhile we also add some\
  \ unique features that commercial chips don't have.\r\n\r\nWe hope more people can\
  \ come and think about the opensource activity in the radio chip domain, and invest\
  \ more in this domain!\r\n\r\nWe are also eager to seek people's voice and help about\
  \ the idea of: Low cost SDR openwifi dongle (+/-200usd) and chip\
  \ tape out!"
themes:
- Hardware
title: openwifi
website: https://github.com/open-sdr/openwifi
show_on_overview: true
chatroom: openwifi
---