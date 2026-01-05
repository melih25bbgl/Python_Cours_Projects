import random
from game_data import data
from art import logo , vs

def format_data(item):
    return f"{item['name']}, a {item['description']}, from {item['country']}"

score = 0
again = True
print(logo)
while again:
    account_a = random.choice(data)
    account_b = random.choice(data)
    while account_b == account_a:
        account_b = random.choice(data)

    print(f"\nCompare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']

    correct_answer = 'a' if a_followers > b_followers else 'b'

    if guess == correct_answer:
        score += 1
        print(f"Correct! Current score: {score}")
        account_a = account_b
    else:
        print(f"Wrong! Final score: {score}")
        score = 0
        again_choice = input("Would you like to play again? (Y/N): ").lower()
        if again_choice == 'n':
            again = False