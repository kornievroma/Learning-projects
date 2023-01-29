import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_images = [rock, paper, scissors]

user_chose = int(input(f"What you choose: 0 for Rock,1 for Paper,2 for Scissors?\n"))
if user_chose >= 3 or user_chose < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_chose])

    comp_choose = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[comp_choose])

    if user_chose == 0 and comp_choose == 2:
        print("User win!")
    elif comp_choose == 0 and user_chose == 2:
        print("You lose")
    elif comp_choose > user_chose:
        print("You lose")
    elif user_chose > comp_choose:
        print("User win!")
    elif comp_choose == user_chose:
        print("It's a draw")
