---
title: openwifi
themes:
 - Hardware
website: https://github.com/open-sdr/openwifi
logo: stands/openwifi/logo.png
description: |
    openwifi: opensource WiFi chip!

Features:
802.11a/g/n
20MHz bandwidth; 70 MHz to 6 GHz frequency range
Mode tested: Ad-hoc; Station; AP, Monitor
DCF (CSMA/CA) low MAC layer in FPGA (10us SIFS is achieved)
Configurable channel access priority parameters:
    duration of RTS/CTS, CTS-to-self
    SIFS/DIFS/xIFS/slot-time/CW/etc
Time slicing based on MAC address
Easy to change bandwidth and frequency:
    2MHz for 802.11ah in sub-GHz
    10MHz for 802.11p/vehicle in 5.9GHz
CSI (Channel State Information, freq offset, equalizer to computer)
IQ capture (real-time AGC, RSSI, IQ sample to computer)
On roadmap: 802.11ax

showcase: |
    All of those opensource hardware projects are focusing on the CPU side:
RISC-V, all kinds of open CPU cores, Raspberry PI, xxxx PI, PINE64, openWRT, AI/machine-learning accelerators.
However the radio connectivity part of those opensource hardware boards are still from black-box silicon (commercial chips, like WiFi chips from big companies).
Openwifi project, which was announced in the last FOSDEM, is the first attempt to build an opensource chip in the radio connectivity domain!
Now we have tested the design on the FPGA development board (SDR -- Software Defined Radio), and it works well in the real world scenario. Meanwhile we also add some unique features that commercial chips don't have.

We hope more people can come and think about the opensource activity in the radio chip domain, and invest more in this domain!

We are also eager to hear from people about the idea (under internal preparation): Low cost SDR openwifi dongle (<100usd) and chip tape out plan.

new_this_year: |
    1. Port the design from a single type of board to 6 types of boards! From high end (expensive) to low end (cheap for entry)
2. Low latency ping: 200~300us round trip.
3. Important improvement on stability and performance.
4. Increase the packet queue from 2 to 4 in FPGA, meet the Linux mac80211 requirement/assumption better.
5. Channel estimation and bug fix on the OFDM receiver. Better reception performance.
6. CSI (Channel State Information) interface to Linux. And it doesn't affect normal WiFi communication.
7. IQ sample interface to Linux. And it doesn't affect normal WiFi communication.
8. Low cost SDR openwifi dongle (<100usd) and chip tape out plan are under preparation. Stay tuned!

layout: stand
---
Welcome to the openwifi stand!
