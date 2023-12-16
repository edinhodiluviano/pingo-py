import unittest

import pingo
from pingo.detect import check_board
from pingo.test import level0, level1

running_on_galileo = check_board(pingo.intel.Edison)


class EdisonTest(unittest.TestCase):
    def setUp(self):
        self.board = pingo.intel.Edison()
        # Level0 Parameters
        self.digital_output_pin_number = 6
        self.digital_input_pin_number = 3
        self.total_pins = 20

        # Level1 Parameters
        self.analog_input_pin_number = 'A3'
        self.expected_analog_input = 4096
        self.expected_analog_ratio = 0.98

    def tearDown(self):
        pass
        # self.board.cleanup()


@unittest.skipIf(not running_on_galileo, 'Edison not detected')
class EdisonBasics(EdisonTest, level0.BoardBasics):
    def test_list_pins(self):
        pin = self.board.pins[self.digital_output_pin_number]
        assert isinstance(pin, pingo.DigitalPin)

        data_pins = len(self.board.pins)
        assert data_pins == self.total_pins


@unittest.skipIf(not running_on_galileo, 'Edison not detected')
class EdisonExceptions(EdisonTest, level0.BoardExceptions):
    pass


@unittest.skipIf(not running_on_galileo, 'Edison not detected')
class EdisonAnalogRead(EdisonTest, level1.AnalogReadBasics):
    pass


@unittest.skipIf(not running_on_galileo, 'Edison not detected')
class EdisonAnalogExceptions(EdisonTest, level1.AnalogExceptions):
    pass


if __name__ == '__main__':
    unittest.main()
