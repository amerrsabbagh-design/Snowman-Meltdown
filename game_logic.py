from ascii_art import STAGES
import random


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")
    # For now, display the initial game state.
    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Prompt user for one guess (logic to be enhanced later)
        guess = input("Guess a letter: ").strip().lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.\n")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.\n")
            continue
        if guess in secret_word:
            guessed_letters.append(guess)
        else:
            mistakes += 1
            if mistakes == max_mistakes:
                print("Game Over! The word was:", secret_word)
        # WIN CHECK AFTER UPDATING STATE
        if set(secret_word).issubset(set(guessed_letters)):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("You saved the snowman! The word was:", secret_word)
            return