import random

secret_number = random.randint(1, 20)
attempts = 0
max_attempts = 5

guess = int(input('Guess the number between 1-20 ("You Will Lose If You Reach 5 Attempts!") : '))

while guess != secret_number:
    if guess > 20 or guess < 1:
        print('Invalid number! You must guess between 1 and 20. YOU LOSE!')
        break

    attempts += 1

    if attempts == max_attempts:
        print(f"You Lose! ({max_attempts} Attempts Reached)")
        break

    if guess > secret_number:
        guess = int(input(f"Oops! You guessed incorrectly {attempts} times! Try a smaller number: "))
    else:  # guess < secret_number
        guess = int(input(f"Oops! You guessed incorrectly {attempts} times! Try a bigger number: "))

if guess == secret_number:
    attempts += 1 
    print(f"Hurra! You Got It in {attempts} attempts!")
