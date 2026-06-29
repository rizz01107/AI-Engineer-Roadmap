print("=" * 40)
print("      NUMBER GUESSING GAME")
print("=" * 40)

secret_number = 7
attempts = 0

print("I have selected a number between 1 and 10.")
print("Can you guess it?")

while True:

    guess = int(input("\nEnter your guess: "))
    attempts += 1

    if guess == secret_number:
        print("\n Congratulations!")
        print(f"You guessed the number in {attempts} attempt(s).")
        break

    elif guess < secret_number:
        print(" Too Low! Try Again.")

    else:
        print(" Too High! Try Again.")

print("=" * 40)
print("Game Over!")
print("=" * 40)