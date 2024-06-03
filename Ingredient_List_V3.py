import time

print("Hello there! Welcome to the guessing game. I want you to guess three items in the pancake ingredient list ")
pancake_ingredients = ["flour", "eggs", "milk", "sugar", "water", "salt"]
score = 0
guessed_list = []    #we create a guess list to track selections
#we use the guess list to ensure user does not guess the same item twice
for i in range(3):
    ingredient = input("What is your ingredient " + str(i+1)+ "? ").lower()
    #we use .lower() to make sure that the user input is always lowercase
    if ingredient in pancake_ingredients and ingredient not in guessed_list:
        print("Well done on your choice! ")
        score += 1
        guessed_list.append(ingredient) #we use append to add the ingredient to the guess list
    elif ingredient in guessed_list:
        print("Incorrect, you chose the same thing! ")
        #you can also do score = score + 1
        #or score += 1, where the plus adds 1 to the score
    else:
        print("Uh no!, incorrect choice! ")
        time.sleep(1.5)
print("Well done for playing! Your score is " + str(score) + " points") 
# remember casting of the data type, such as here where we use string
time.sleep(1.5)
print("The ingredient list was: ")
print(pancake_ingredients)