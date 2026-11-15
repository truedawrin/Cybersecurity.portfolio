import random

num = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number between 1 and 100: \n")) 
        if guess > num:
            print("\nTo high! guess again")
        elif guess < num:
            print("\nTo low! guess again")
        elif guess == num:
            print("\nCongrats! you guessed it!")
            break
    except ValueError:
        print("Please enter a valid number.\n")    
