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



import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

hand = [rock, paper, scissors]

computer_choice = random.randint(0, 2)

if user_choice == computer_choice :
    print(f"{hand[user_choice]} \n Computer chose: \n {hand[computer_choice]} \n It's a draw!")
elif user_choice == 0 and computer_choice == 2 :
    print(f"{hand[user_choice]} \n Computer chose: \n {hand[computer_choice]} \n You win!")
elif user_choice == 1 and computer_choice == 0:
    print(f"{hand[user_choice]} \n Computer chose: \n {hand[computer_choice]} \n You win!")
elif user_choice == 2 and computer_choice == 1:
    print(f"{hand[user_choice]} \n Computer chose: \n {hand[computer_choice]} \n You win!")
else :
    print(f"{hand[user_choice]} \n Computer chose: \n {hand[computer_choice]} \n You lose!")
    