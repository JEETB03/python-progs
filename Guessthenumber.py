import random

print("""
  ________                                __  .__              _______               ___.                ._.
 /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____    \      \  __ __  _____\_ |__   ___________| |
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \ |
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/\|
 \______  /____/  \___  >____  >____  >  |__| |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   __
        \/            \/     \/     \/             \/     \/          \/            \/    \/     \/       \/
""")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
  attempts = 10
else:
  attempts = 5

while attempts > 0:
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if guess == number:
    print(f"You got it! The answer was {number}.")
    break
  elif guess > number:
    print("Too high.")
  else:
    print("Too low.")
  attempts -= 1
  if attempts == 0:
    print("You've run out of guesses, you lose.")