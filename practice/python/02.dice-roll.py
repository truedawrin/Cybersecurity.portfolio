import random

SIDES = 6

while True:
    choice = input("Roll the dice? (y/n): ").lower().strip()
    if choice == "y":
        dice1 = random.randint(1, SIDES)
        dice2 = random.randint(1, SIDES)
        print(f"You got a {dice1} and a {dice2} (total: {dice1 + dice2})")
    elif choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice! Please enter y or n.")
