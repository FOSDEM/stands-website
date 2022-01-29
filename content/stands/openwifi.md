---
description: |
  <img src="/stands/openwifi/logo-1.png">
  <p>Videos: <a href="https://ftp.heanet.ie/mirrors/fosdem-video/2022/stands/openwifi/stand_video_openwifi_video1.webm">The 1st demo</a>, 
  <a href="https://video.fosdem.org/2022/stands/openwifi/stand_video_openwifi_video2.webm">Flash 2020</a>, 
  <a href="https://video.fosdem.org/2022/stands/openwifi/stand_video_openwifi_video3.webm">Low latency gaming</a>, 
  <a href="https://video.fosdem.org/2022/stands/openwifi/stand_video_openwifi_video4.webm">FOSDEM 2020</a>, 
  <a href="https://video.fosdem.org/2022/stands/openwifi/stand_video_openwifi_video5.webm">Libreplanet 2021</a>
  </p>
  <p>There are many WiFi chips around us. The WiFi router, the smart light, the TV, the phone, etc., all have WiFi chips inside. Ever imagine replacing those chips with an open-source chip?</p>
  <p><a href="https://github.com/open-sdr">openwifi</a>, announced in FOSDEM’20, is the 1st opensource WiFi chip design (802.11a/g/n, ax is coming) which includes Verilog source code for the chip and C source code for the Linux driver.</p>
  <p>We have paved solid steps towards an open-source WiFi chip. Now if you have commercial off the shelf FPGA boards, you can download our design onto your board and start to use this FPGA based WiFi in the same way as other commercial WiFi chips! The FPGA board could become WiFi AP, WiFi client, ad-hoc node or sniffer, etc. Just like a Raspberry PI! Besides the standard WiFi functionality, it also has some special features.</p>

  <ul>
    <li>802.11a/g/n (802.11ax/WiFi6 is under development)</li>
    <li>20MHz bandwidth; 70 MHz to 6 GHz frequency range</li>
    <li>Mode tested: Ad-hoc; Station; AP, Monitor</li>
    <li>DCF (CSMA/CA) low MAC layer in FPGA (10us SIFS is achieved)</li>
    <li>802.11 packet injection and fuzzing</li>
    <li>CSI sensing: Channel State Information, freq offset, equalizer to computer</li>
    <li>CSI fuzzer -- anti sensing: Create artificial channel response in WiFi transmitter</li>
    <li>[IQ capture]: real-time AGC, RSSI, IQ sample to computer. [Dual antenna version]</li>
    <li>Configurable channel access priority parameters: duration of RTS/CTS, CTS-to-self, SIFS/DIFS/xIFS/slot-time/CW/etc</li>
    <li>Time slicing based on MAC address (time gated/scheduled FPGA queues)</li>
    <li>Easy to change bandwidth and frequency: 2MHz for 802.11ah in sub-GHz; 10MHz for 802.11p/vehicle in 5.9GHz</li>
  </ul>

layout: stand
logo: stands/openwifi/logo.png
new_this_year: |
  <p>Checkout openwifi update in these events this year:</p>
  <ul>
    <li>Feb 6 11:20 (Brussels time): <a href="https://fosdem.org/2022/schedule/event/openwifipynqz1/">Bring openwifi to PYNQ-Z1 with ultra low cost</a> in Libre-Open VLSI and FPGA devroom.</li>
    <li>Feb 6 13:10 (Brussels time): <a href="https://fosdem.org/2022/schedule/event/radio_openwifi/">Opensource WiFi chip (openwifi) progress and future plan</a> in Free Software Radio devroom.</li>
  <p>Also feel free come to us for further discussion!</p>
  </ul>
showcase: "All of those opensource hardware projects are focusing on the CPU side:\r\
  \nRISC-V, all kinds of open CPU cores, Raspberry PI, many other PI, PINE64, openWRT, AI/machine-learning\
  \ accelerators.\r\nHowever the radio connectivity part of those opensource hardware\
  \ boards are still from black-box silicon (commercial chips, like WiFi chips from\
  \ big companies).\r\nOpenwifi project, which was announced in the FOSDEM'20, is\
  \ the first attempt to build an opensource chip in the radio connectivity domain!\r\
  \nNow we have tested the design on the FPGA development board (SDR -- Software Defined\
  \ Radio), and it works well in the real world scenario. Meanwhile we also add some\
  \ unique features that commercial chips don't have.\r\n\r\nWe hope more people can\
  \ come and think about the opensource activity in the radio chip domain, and invest\
  \ more in this domain!\r\n\r\nWe are also eager to seek people's voice and help about\
  \ the idea of: Low cost SDR openwifi dongle (100usd?) and chip\
  \ tape out!"
themes:
- Hardware
title: openwifi
website: https://github.com/open-sdr/openwifi
show_on_overview: true
chatroom: openwifi
---
