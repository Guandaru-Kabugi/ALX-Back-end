# try:
#   # Code that might raise an exception
#   pass
# except ExceptionType:
#   # Code to handle the exception
# else:
#     pass
#   # Code that executes if no exception occurs
# finally:
#   # Code that always executes, regardless of exceptions

# def divide(x, y):
#   if y == 0:
#     raise ZeroDivisionError("Division by zero is not allowed")
#   return x / y

# answer = divide(2,0)
# print(answer)
class MyKeyError(Exception):
    def __init__(self, item_name):
        self.name = item_name
    def __str__(self,) -> str:
        return f"Sorry, '{self.name}' is not available in our inventory."
class OutOfStockError(Exception):
    """Custom exception for handling out-of-stock items."""

    def __init__(self, item_name):
        self.name = item_name

    def __str__(self):
        return f"Sorry, the item '{self.name}' is out of stock."
# Sample Product Inventory
product_inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 0,  # Out of stock
    "grapes": 3,
    "beetroot": 0
}
def purchase_item(item, quantity):
    try:
        if item not in product_inventory:
            raise MyKeyError(item)
        if product_inventory[item] == 0:
            raise OutOfStockError(item)
    except (OutOfStockError, MyKeyError) as e:
        print(e)
    else:
        print(f"Purchase successful: {quantity} {item}(s)")
        product_inventory[item] -= quantity
# Testing the Custom Exception
try:
    purchase_item("apple", 3)  # Purchase successful
    purchase_item("orange", 1)  # Raises OutOfStockError
    purchase_item("watermelon", 1)  # Item not available
    purchase_item("Avocado", 2)  # Item not available
except (OutOfStockError, MyKeyError) as e:
    print(e)  # Output: