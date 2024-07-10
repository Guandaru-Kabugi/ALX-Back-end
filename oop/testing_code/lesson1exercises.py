import unittest


# def square_function(a,b):
    
#     results = a * b
#     return results
# anaswer = square_function(3,4)
# # print(anaswer)

# class CheckEqualSides(unittest.TestCase):
#     def setUp (self):
#         self.a = 3
#         self.b = 4
#     def test_approach_1(self):
#         results = square_function(self.a,self.b)
#         self.assertEqual(results,self.a * self.a,msg="Numbers need to be equal")
#     def test_approach_2(self):
#         results = square_function(self.a,self.b)
#         self.assertEqual(results,self.b*self.b, msg="numbers need to be equal")



# if __name__ == "__main__":
#     unittest.main()
class UnequalNumberError(Exception):
    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2
    def __str__(self) -> str:
        return f"The {self.number1} is not equal to {self.number2}."
        

def square_function(a,b):
    try:
        if a != b:
            raise UnequalNumberError(a,b)
    except UnequalNumberError as e:
        print(e)
    else:
        results = a * b
        print (results)
anaswer = square_function(4,5)
