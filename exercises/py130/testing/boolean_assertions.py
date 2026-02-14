# boolean assertion, will fail if value is not odd
import unittest

class TestSomething(unittest.TestCase):
    def test_value_is_odd(self):
        value = 3
        self.assertTrue(value % 2 == 0, 'value is not odd')

unittest.main()