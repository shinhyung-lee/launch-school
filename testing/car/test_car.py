import unittest 
from car import Car 

class CarTest(unittest.TestCase):
    def setUp(self):
        self.car = Car()
        
    def test_value_equalit(self):
        car1 = Car()
        car2 = Car()
        
        car1.name = "kim"
        car2.name = "kim"
        
        self.assertEqual(car1, car2)

if __name__ == "__main__":
    unittest.main(verbosity=2)