---
description: |
  Openwifi, announced in FOSDEM’20, is the 1st opensource WiFi chip design (802.11a/g/n) which includes Verilog source code for the chip and C source code for the Linux driver. Currently the design runs on FPGA verification platform via SDR (Software Defined Radio) methodology. With the design running, the FPGA board could become WiFi AP, WiFi client, ad-hoc node or sniffer. Besides the standard WiFi functionality (802.11a/g/n), it also has some special features, such as non-standard frequencies (<6GHz); CSI; IQ sample; configurable low MAC behavior; time slicing; etc.

  <ul>
    <li>802.11a/g/n</li>
    <li>20MHz bandwidth; 70 MHz to 6 GHz frequency range</li>
    <li>Mode tested: Ad-hoc; Station; AP, Monitor</li>
    <li>DCF (CSMA/CA) low MAC layer in FPGA (10us SIFS is achieved)</li>
    <li>802.11 packet injection</li>
    <li>CSI (Channel State Information, freq offset, equalizer to computer)</li>
    <li>IQ capture (real-time AGC, RSSI, IQ sample to computer)</li>
    <li>Configurable channel access priority parameters: duration of RTS/CTS, CTS-to-self, SIFS/DIFS/xIFS/slot-time/CW/etc</li>
    <li>Time slicing based on MAC address (time gated/scheduled FPGA queues)</li>
    <li>Easy to change bandwidth and frequency: 2MHz for 802.11ah (sub-GHz); 10MHz for 802.11p/vehicle (5.9GHz)</li>
    <li>On roadmap: 802.11ax</li>
  </ul>
  <p>
  <video width=\"100%\" controls>
    <source src=\"https://video.fosdem.org/2021/stands/openwifi/openwifi_video1.mp4\" type=\"video/mp4\">
  </video>
  <p>

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
