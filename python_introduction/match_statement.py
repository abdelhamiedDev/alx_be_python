import random

print("Welcome to the Number Guessing Game!")

while True:

    secret_number = random.randint(1, 10)
    print("I'm thinking of a number between 1 and 10. Can you guess it?")

    guess = int(input())

    match guess:
        case _ if guess < secret_number:
            print("Too low! Try again.")
        case _ if guess > secret_number:
            print("Too high! Try again.")
        case _:
            print("Congratulations! You've guessed the number!")
            print ("Do you want to play again? (yes/no)")
            
            play_again = input().lower()

            match play_again:
                    case 'yes':
                        continue
                    case 'no':
                        print("Thank you for playing! Goodbye!")
                        break
                    case _:
                        print("Invalid input. Exiting the game.")
                        break
