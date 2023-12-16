"""

This example is controlled by the knob in A0
It shows the level of power on the display
and lights a PWM Led on 6 (or the dicimal point)
"""

import time
from pprint import pprint

import pingo

board = pingo.detect.get_board()

pot = board.pins['A0']
pot.mode = pingo.ANALOG

led = board.pins[6]
led.mode = pingo.PWM

display_pins = [board.pins[i] for i in range(8, 14) + [7]]
seg_display = pingo.parts.led.SevenSegments(*display_pins)
for pin in display_pins:
    pin.mode = pingo.OUT


def bar(pin):
    reading = pot.ratio()
    n = int(reading * 10)
    seg_display.digit = n
    led.value = reading


pprint(board.pins, indent=4, width=1)

while True:
    bar(pot)
    time.sleep(0.05)
