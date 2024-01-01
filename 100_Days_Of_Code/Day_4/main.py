import random

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

options = [rock, paper, scissors]

user_option = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_option = random.randint(0, 2)

print(f"{options[user_option]}\n")
print(f"Computer chose:\n{options[computer_option]}\n")

if user_option == computer_option:
    print("It's a draw")
elif ((options[user_option] == rock and options[computer_option] == paper) or
      (options[user_option] == paper and options[computer_option] == scissors) or
      (options[user_option] == scissors and options[computer_option] == rock)):
    print("You lose!")
else:
    print("You win!")
