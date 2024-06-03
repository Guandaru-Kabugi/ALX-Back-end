import time

print("Hello there! Welcome to the guessing game. I want you to guess three items in the pancake ingredient list ")
pancake_ingredients = ["flour", "eggs", "milk", "sugar", "water", "salt"]
score = 0
ingredient_1 = input("What is your first ingredient? ")
if ingredient_1 in pancake_ingredients:
    print("Well done on your choice! ")
    score += 1
    #you can also do score = score + 1
    #or score += 1, where the plus adds 1 to the score
else:
    print("Uh no!, incorrect choice! ")
    time.sleep(1.5)
ingredient_2 = input("What is your second ingredient? ")
if ingredient_2 in pancake_ingredients:
    print("Well done on your choice! ")
    score += 1
else:
    print("Uh no!, incorrect choice! ")
    time.sleep(1.5)
ingredient_3 = input("What is your third ingredient? ")
if ingredient_3 in pancake_ingredients:
    print("Well done on your choice! ")
    score += 1
else:
    print("Uh no!, incorrect choice! ")
print("Well done for playing! Your score is " + str(score) + " points") 
# remember casting of the data type, such as here where we use string
time.sleep(1.5)
print(pancake_ingredients)