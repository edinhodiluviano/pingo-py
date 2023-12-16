import unittest

import pingo
from pingo.detect import check_board, has_module
from pingo.test import level0

running_on_raspberry = check_board(pingo.rpi.RaspberryPi)


class RaspberryTest(unittest.TestCase):
    def setUp(self):
        self.board = pingo.rpi.RaspberryPi()
        self.vdd_pin_number = 2
        self.digital_output_pin_number = 13
        self.digital_input_pin_number = 26
        self.total_pins = 26

    def tearDown(self):
        self.board.cleanup()


@unittest.skipIf(not running_on_raspberry, 'RaspberryPi not detected')
@unittest.skipIf(
    not has_module('RPi'),
    'pingo.rpi requires RPi.GPIO installed',
)
class RaspberryBasics(RaspberryTest, level0.BoardBasics):
    pass


@unittest.skipIf(not running_on_raspberry, 'RaspberryPi not detected')
@unittest.skipIf(
    not has_module('RPi'),
    'pingo.rpi requires RPi.GPIO installed',
)
class RaspberryExceptions(RaspberryTest, level0.BoardExceptions):
    pass


if __name__ == '__main__':
    unittest.main()
