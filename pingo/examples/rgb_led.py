import time

import pingo

board = pingo.detect.get_board()

rgb = [board.pins[i] for i in (11, 13, 15)]

for pin in rgb:
    pin.mode = pingo.OUT
    pin.low()

while True:
    for pin in rgb:
        pin.low()
        print(pin, pin.state)
        time.sleep(0.5)
        pin.high()
    break
