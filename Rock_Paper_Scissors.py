rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game = [rock, paper, scissors]

hand_length = len(game)

choice = random.randint(0, hand_length - 1)

computer_choice = game[choice]

# computer_choice = random.choice(game)


players_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors:\n "))


if players_choice > 2:
    print("You chose an invalid number. You lose!")
else:
    print(f"Your choice {game[players_choice]}")
    print(f"Computer chose {computer_choice}")
    


        
 
    if players_choice == choice:
        print("You draw!")
        
    if players_choice > choice:
        if players_choice == 2 and choice == 0:
            print("You lose!")
        else:
            print("You win")
            
    elif players_choice < choice:
        if choice  == 2 and players_choice == 0:
            print("You win!")
            
        else:
            print("You lose!")
