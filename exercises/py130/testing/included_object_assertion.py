import unittest

class TestSomething(unittest.TestCase):
    def test_xyz_in_lst(self):
        lst = ['abc', 'xyz']
        # Your code here
        self.assertIn('xyz', lst)

unittest.main()