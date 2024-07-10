# class Learner:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def learner_information (self):
#         print (f"The student's name is {self.name} and their age is {self.age}")
    
# student_1 = Learner("Alex", 27)
# student_2 = Learner("Grace", 26)
# student_1.learner_information()
# student_2.learner_information()
class ProductCatalog:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_value = 0
    def total_value_products (self):
        product_value = self.price * self.quantity
        self.total_value+=product_value
        return self.total_value
    def print_total_value (self):
        print(f"The total value for {self.name} is {self.total_value}")

rice = ProductCatalog("Rice", 200, 400)
wheat_flour = ProductCatalog("Wheat Flour", 150, 40)
Maize_flour = ProductCatalog("Maize Flour", 100, 100)
products = [rice, wheat_flour, Maize_flour]
for product in products:
    product.total_value_products()
    product.print_total_value()