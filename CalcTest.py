import unittest
from Calc import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5
    
    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(5, 2)
        self.assertEqual(result, 3) # Expect 5 - 2 = 3
    
    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(4, 3)
        self.assertEqual(result, 12)

    def test_divide(self):
        calc = Calculator()
        result = calc.divide(7, 2)
        self.assertEqual(result, 3.5)
        self.assertIsInstance(result, float) 
        with self.assertRaises(ValueError):
            calc.divide(5, 0)



if __name__ == "__main__":
    unittest.main()