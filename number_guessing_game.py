import random
def game_loop(computer_number,choo = ""):
    is_correct = False
    counter = 0
    if choo == "easy":
        counter = 10
    elif choo == "hard":
        counter = 5
    else:
        print("Invalid error!")
        return 1
    while not is_correct:
        print(f"You have {counter} attemps remaining to guess the number.")
        user_number = int(input("Make a guess: "))
        if counter > 1 and user_number <  computer_number:
            print("Too low.")
            print("Guess again.")
            counter -= 1
        elif counter > 1 and user_number >  computer_number:
            print("Too High.")
            print("Guess again.")
            counter -= 1
        elif counter > 1 and user_number ==  computer_number:
            print("You Win!")
            print(f"I'am number is {computer_number}")
            is_correct = True
            counter -= 1
        else:
            print("!!You Lose!!")
            print(f"I'am number is {computer_number}")
            is_correct = True
            counter -= 1
print("Welcome to the Number Guessing Game")
continu = True
while continu:
    print("I'm thinking of a number between 1 and 100.")
    computer_num = random.randint(1,100)
    choos = input("Choose a difficulty. Type 'easy' or 'hard' ")
    game_loop(computer_num,choos)
    again = input("Would you like to play again? 'y' or 'n':")
    if again == "n":
        continu = False