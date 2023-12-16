"""
Pushbutton led.

The led comes on when you press the button.

Connections example found on ./button.png
"""
# -*- coding: utf-8 -*-
import sys

import pingo

try:
    print('Loading board...')
    board = pingo.detect.get_board()
    print('Its ok...')
except Exception as e:
    print(f'Error on get_board: {e}')
    sys.exit(1)

led_pin = board.pins[13]
led_pin.mode = pingo.OUT
button_pin = board.pins[5]
button_pin.mode = pingo.IN

while True:
    if button_pin.state == pingo.HIGH:
        led_pin.hi()
    else:
        led_pin.lo()
