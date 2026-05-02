import random
while True:
    attempts = 7
    number = random.randint(1, 100)
    print("Welcome to the Guess the Number Game!")
    print(f"You have {attempts} attempts to guess the number.")
    while attempts > 0:
        guess = int(input("Enter your guess between 1 and 100: "))
        if guess == number:
            print("-"*10 + "You guessed the number correctly! Congratulations!"+"-"*10)
            break
        elif guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        attempts -= 1
        print(f"You have {attempts} attempts left.")
    if attempts == 0:
        print(f"Sorry, you're out of attempts. The number was {number}.")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thank you for playing! Goodbye!")
        break