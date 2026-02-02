import unittest 
from car import Car

class EqualityTest(unittest.TestCase):
    def test_value_equality(self):
        car1 = Car()
        car2 = Car()
        
        car1.name = 'mophie'
        car2.name = 'mophie'
        
        self.assertEqual(car1, car2)
        self.assertIs(car1, car2)
        
if __name__ == "__main__":
    unittest.main()