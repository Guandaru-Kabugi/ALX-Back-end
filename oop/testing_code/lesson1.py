import unittest

# def add(x, y):
#   """Returns the sum of two numbers."""
#   return x + y

# class TestAdd(unittest.TestCase):

#   def test_add_positive(self):
#     result = add(5, 3)
#     self.assertEqual(result, 8)

#   def test_add_negative(self):
#     result = add(-2, 7)
#     self.assertEqual(result, 5)

# if __name__ == "__main__":
#   unittest.main()
  
def division (x,y):
    try:
        if x == 0 or y == 0:
            raise ZeroDivisionError
        results = x/y
    except ZeroDivisionError:
        return "Cannot divide a number by Zero"
    else:
        return results
    
class TestDivision (unittest.TestCase):
    def test_divide_zero_index1(self):
        results = division(0,5)
        results = ZeroDivisionError
        self.assertEqual(results, ZeroDivisionError)
    def test_divide_zero_index2(self):
        results = division(5,0)
        results = ZeroDivisionError
        self.assertEqual(results,ZeroDivisionError)
    def test_divide_two_numbers(self):
        results = division(5,2)
        self.assertEqual(results,2.5)
        
if __name__ == "__main__":
    unittest.main()