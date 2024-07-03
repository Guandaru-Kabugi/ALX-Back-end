import random

number = random.randint(1,10)
print(number)
# play = input("Play again? Type yes or no: ").lower()

guess_counter = 0
continue_playing = True
while continue_playing:
    guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it?:  "))
    match guess:#variable name
        case _ if guess > number and guess<=10:
            print("Oops, your guess is too high. Try again!")
            guess_counter+=1
            print(f"Guess: {guess_counter}")
        case _ if guess < number:
            print("Oops, your guess is too low. Try again!") 
            guess_counter+=1    
            print(f"Guess: {guess_counter}")
        case _ if guess == number: #pattern or input value
            print("Well Done!")
            guess_counter+=1
            print(f"Guess: {guess_counter}")
            play_again = input("Do you want to play again?yes or no: ") .lower()
            if play_again == "yes":
                number = random.randint(1,10)
                print(number)
                guess_counter = 0
                continue
            else:
                continue_playing = False
        case _:
            print("Guess out of range. Please enter a valid number. Try again")
            guess_counter+=1
            print(f"Guess: {guess_counter}")
# print(f"Guess: {guess_counter}")