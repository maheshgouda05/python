
import random

def play_hangman():
    # List of secret fruit names
    fruits = [
        "apple", "mango", "banana", "orange",
        "grapes", "papaya", "cherry", "guava",
        "pineapple", "watermelon"
    ]

    # Select a random fruit
    secret_word = random.choice(fruits)

    # Number of chances = word length + 2
    chances = len(secret_word) + 2

    # Store guessed letters
    guessed_letters = []

    print("===== WELCOME TO HANGMAN =====")
    print("Guess the name of the fruit!")
    print(f"The word contains {len(secret_word)} letters.")
    print(f"You have {chances} chances.")

    while chances > 0:
        # Display guessed letters and underscores
        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word.strip())
        print("Remaining chances:", chances)

        # Check whether the player has guessed the word
        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You won!")
            print("The fruit was:", secret_word)
            return

        guess = input("Guess a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            chances -= 1
            print("Wrong guess!")

    print("\nGame over! You ran out of chances.")
    print("The correct fruit was:", secret_word)


# Start the game
play_hangman()
