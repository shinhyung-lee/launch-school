
import unittest

class TestSomething(unittest.TestCase):
    def test_value_is_none(self):
        value = None
        # Your code here
        self.assertIsNone(value)

unittest.main()