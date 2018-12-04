#!/usr/bin/python3

try:
    import ulamspiral
except Exception as e:
    raise e
import unittest


class ExceptionTest(unittest.TestCase):
    """ Test that proper exceptions are thrown."""

    # UlamSpiral init: start must be an int ##################################
    def test_start_as_float(self):
        self.assertRaises(TypeError, ulamspiral.UlamSpiral, end=24, start=1.5)

    # UlamSpiral init: start must not be string ##############################
    def test_start_as_str(self):
        self.assertRaises(TypeError, ulamspiral.UlamSpiral, end=24, start='a')

    # UlamSpiral init: start may not be negative #############################
    def test_start_negative(self):
        self.assertRaises(ValueError, ulamspiral.UlamSpiral, end=24, start=-1)

    # UlamSpiral init: start may not be too large ############################
    def test_start_large(self):
        self.assertRaises(
            ValueError,
            ulamspiral.UlamSpiral,
            end=24,
            start=4294967299
        )

    # UlamSpiral init: end must be an int ####################################
    def test_end_as_float(self):
        self.assertRaises(TypeError, ulamspiral.UlamSpiral, end=5.5)

    # UlamSpiral init: end must not be a string ##############################
    def test_end_as_str(self):
        self.assertRaises(TypeError, ulamspiral.UlamSpiral, end='a')

    # UlamSpiral init: end may not be negative ###############################
    def test_end_negative(self):
        self.assertRaises(ValueError, ulamspiral.UlamSpiral, end=-24)

    # UlamSpiral init: end may not be too large ##############################
    def test_end_large(self):
        self.assertRaises(ValueError, ulamspiral.UlamSpiral, end=4294967299)

    # UlamSpiral init: end may not be smaller than start #####################
    def test_end_less_than_start(self):
        self.assertRaises(
            ValueError,
            ulamspiral.UlamSpiral,
            end=24,
            start=100
        )


class EqualityTest(unittest.TestCase):
    """ Test equality of __str__  or self.rows of various constructions."""

    # UlamSpiral trivial example #############################################
    def test_example_trivial(self):
        val = [[0]]
        self.assertEqual(ulamspiral.UlamSpiral(0, start=0).rows, val)

    # UlamSpiral less trivial example ########################################
    def test_example_less_trivial(self):
        val = [[0, 1]]
        self.assertEqual(ulamspiral.UlamSpiral(1, start=0).rows, val)

    # UlamSpiral example with start at 1 #####################################
    def test_example_start_zero(self):
        val = ' 21 22 23 24   \n 20  7  8  9 10\n 19  6  1  2 11\n' \
              ' 18  5  4  3 12\n 17 16 15 14 13\n'
        self.assertEqual(str(ulamspiral.UlamSpiral(24)), val)

    # UlamSpiral example with start at 0 #####################################
    def test_example_start_one(self):
        val = ' 20 21 22 23 24\n 19  6  7  8  9\n 18  5  0  1 10\n' \
              ' 17  4  3  2 11\n 16 15 14 13 12\n'
        self.assertEqual(str(ulamspiral.UlamSpiral(24, start=0)), val)


if __name__ == '__main__':
    unittest.main()
