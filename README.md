# ESP-BeagleboneHomeAutomation
This is a kind of home automation system using this two technologies (ESP32 and Beaglebone Black Wireless) 
that establish communication by bluetooth low energy.
Inside of BBB is running a fuzzy-logic system that takes control of the lights and air-conditioned behavior
so they'll always be comfortable for a human. Programmed using Python.
The ESP32 has the job of collect data using sensors, in this case DTH for temperature and hummidity, BH1750 
lightmeter, PIR and a light-dependent resistor (LDR). Programmed using Arduino IDE.
