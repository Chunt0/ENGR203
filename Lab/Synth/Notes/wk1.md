# Christopher Hunt | ENGR 203  |  Week 1 Note
# 5/7
This week we began the final lab for ENGR 203. My goal is to follow along with and build Moritz Klein and Erica Synth's EDU DIY EuroRack. I intend on accomplishing this for, at a minimum, the VCO module and the Mixer.

At the heart of this VCO is a CD40106 - hex schmitt trigger inverter,the output of which is fed back to itself. At this node there is a capacitor to ground and a resistive pathway to ground that is controlled by an emitter follower configuration that takes a control voltage (CV) in which "tunes" the speed at which the capacitor discharges. (5_7_schem.png)

V_out is then buffered using a TL042 Dual Op Amp in a noninverting, voltage following configuration. Once the signal is buffered we use a 1 microF capacitor and a 100k ohm resistor to remove any offset in the signal voltage. It does so by AC coupling. The capacitor in series with the signal only allows the AC oscillations in the voltage to pass while removing any DC offset.

Back to V_out. When the schmitt trigger hits its threshold voltage and turns off, the capacitor at V_out begins to drain, creating the iconic saw tooth pattern. This drain pathway will pass through the NPN transistors collector to its emitter. The base pin is where we will control the rate at which this capacitor discharges.

During lab testing, the base is connected to the wiper of a 100k potentiometer. The waveform read from V_out is oscillating at about 80kHz, far above audio range. When completing the full coarse knob circuitry I was still unable to get the frequency down to a musically useful range. The lowest I was able to get was around 6k6Hz, with 545 mV at the NPN transistors base. According to the VCO manual, this is the highest range voltage tolerated for this VCO. This, however, was achieved by using the lowest possible resistor values for the components the manual suggests. Perhaps if the trim pot is put in series with a 500 ohm resistor? Anyway, more testing needs to be done to ensure proper base voltage ranges to acquire the correct output frequency.

The AC coupling and voltage following appears to be working swimmingly. Something I've noticed just now is that as I leave the system the voltage at the NPN base drifts lower. I just caught it at roughly 450 mV, outputting a 600 Hz signal. I bumped the circuit and it jumped back to 550 mV. So far it seems like the circuit is very unstable.


# Links:
https://www.ericasynths.lv/shop/diy-kits-1/edu-diy-vco/

https://www.ericasynths.lv/shop/diy-kits-1/edu-diy-mixer/