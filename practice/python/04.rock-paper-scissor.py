import random


        
emojis = { "r": "🪨", "s": "✂️", "p": "📃"}
options = tuple(emojis.keys())

def get_player_choice():
    while True: 
        player_choice = (input("Rock, paper, scissors? (r/p/s) \n")).lower().strip()
        if player_choice in options:
            return player_choice
        else:
            print("Invalid choice!")
            continue
def display_choice(player_choice, computer_choice):
    print(f"You chose {emojis[player_choice]}\ncomputer chose {emojis[computer_choice]}")

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        print("its a Tie!")

    elif (player_choice == "r" and computer_choice == "s") or \
         (player_choice == "s" and computer_choice == "p") or \
         (player_choice == "p" and computer_choice == "r"):
        print("You win!")
    else:
        print("You lose")

def play_game():
    while True:
        player_choice = get_player_choice()
        
        computer_choice = random.choice(options)        
        
        display_choice(player_choice, computer_choice)
        
        determine_winner(player_choice, computer_choice)

        try_again = input("Continue? (y/n): ").lower().strip()
        if try_again == "n":
            break
        elif try_again == "y":
            continue
        else:
            print("enter a valid choice!")
            break

play_game() 
