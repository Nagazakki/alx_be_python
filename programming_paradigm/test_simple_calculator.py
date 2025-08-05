import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        result = self.calc.add(2, 3)
        assert result == 5
    
    def test_subtraction(self):
        result = self.calc.subtract(10, 5)
        assert result == 5
    
    def test_multiply(self):
        result = self.calc.multiply (3, 4)
        assert result == 12
    
    def test_divide(self):
        result = self.calc.divide(10, 2)
        assert result == 5
    
    def test_divide_by_zero(self):
        result = self.calc.divide(10, 0)
        assert result is None

if __name__ == '__main__':
    unittest.main()