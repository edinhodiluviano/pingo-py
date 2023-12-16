from time import sleep

import pingo

rpi = pingo.rpi.RaspberryPi()

#                 F   A  B   G   E   D   C   G
led_sequence = [13, 11, 7, 15, 26, 24, 21, 15]

pins = [rpi.pins[loc] for loc in led_sequence]

for pin in pins:
    pin.mode = pingo.OUT
    pin.low()

prev_pin = pins[-1]
while True:
    for pin in pins:
        pin.high()
        sleep(0.11)
        prev_pin.low()
        prev_pin = pin
