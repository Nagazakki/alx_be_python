import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
    
    def test_divide_by_zero(self):
        result = self.calc.divide(10, 0)
        assert result is None

if __name__ == '__main__':
    unittest.main()