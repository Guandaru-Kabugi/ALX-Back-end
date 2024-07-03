def called (name):
    print(f"Hello {name}")
called("Alex")

def area (length,width):
    area = length * width
    return area

calculated_area= area(10,5)
print(calculated_area)

def even_or_odd (number):
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")
even_or_odd(7)        