import random

def choose_word():
    # List of possible words
    words = ["python", "java", "hangman", "programming", "algorithm", "function", "variable"]
    return random.choice(words)

def display_game_state(word, guessed_letters, attempts):
    # Display the current state of the word with guessed letters
    display_word = [letter if letter in guessed_letters else "_" for letter in word]
    print("Word: ", " ".join(display_word))
    print(f"Attempts left: {attempts}")
    print("Guessed letters: ", " ".join(guessed_letters))

def play_game():
    word = choose_word()
    guessed_letters = []
    attempts = 6  # Number of attempts

    print("Welcome to Hangman!")

    while attempts > 0:
        display_game_state(word, guessed_letters, attempts)
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        
        guessed_letters.append(guess)

        if guess in word:
            print(f"Good job! {guess} is in the word.")
        else:
            attempts -= 1
            print(f"Sorry, {guess} is not in the word.")

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(f"Out of attempts! The word was: {word}")

if __name__ == "__main__":
    play_game()
