import art
import random
from replit import clear
import game_data

def game():
    print(art.logo)
    score = 0
    game_should_continue = True
    account_a = random.choice(game_data.data)
    account_b = random.choice(game_data.data)
    while game_should_continue:
        account_a = account_b
        account_b = random.choice(game_data.data)
        while account_a == account_b:
            account_b = random.choice(game_data.data)
        print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
        print(art.vs)
        print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        clear()
        print(art.logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

def check_answer(guess, a_followers, b_followers):
  if guess == "a":
    return a_followers > b_followers
  else:
    return b_followers > a_followers

game()