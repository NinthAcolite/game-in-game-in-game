import json
import random


def load_words_from_json(file_path):
    with open(file_path, "r", encoding="utf-8") as json_file:
        words_data = json.load(json_file)
        return words_data["words"]


def choose_random_word(words_list):
    return random.choice(words_list)


def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word


def draw_hangman(attempts_left):
    hangman_stages = [
        """
        +---+
        |   |
            |
            |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
       /    |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        =========
        """,
    ]
    return hangman_stages[6 - attempts_left]


def main():
    json_file_path = "words.json"  # Путь к вашему файлу JSON с словами
    words_list = load_words_from_json(json_file_path)
    secret_word = choose_random_word(words_list)
    guessed_letters = []

    max_attempts = 6
    while max_attempts > 0:
        current_display = display_word(secret_word, guessed_letters)
        print(f"Current word: {current_display}")
        print(draw_hangman(max_attempts))

        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in secret_word:
            guessed_letters.append(guess)
            print("Correct!")
        else:
            max_attempts -= 1
            print(f"Wrong! You have {max_attempts} attempts left.")

        if current_display == secret_word:
            print(f"Congratulations! You've guessed the word: {secret_word}")
            break

    if max_attempts == 0:
        print(f"Game over! The word was: {secret_word}")


if __name__ == "__main__":
    main()
