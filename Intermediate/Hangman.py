"""
Intermediate Task 2: Hangman
- Word-guessing with visual progress and hints.
"""
import random
import string

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""" ,
    """
     +---+
     O   |
         |
         |
        ===""" ,
    """
     +---+
     O   |
     |   |
         |
        ===""" ,
    """
     +---+
     O   |
    /|   |
         |
        ===""" ,
    """
     +---+
     O   |
    /|\  |
         |
        ===""" ,
    """
     +---+
     O   |
    /|\  |
    /    |
        ===""" ,
    """
     +---+
     O   |
    /|\  |
    / \  |
        ===""" ,
]

WORDS = {
    "animal": ["tiger", "giraffe", "elephant", "kangaroo", "panther"],
    "fruit": ["banana", "apple", "orange", "mango", "papaya"],
    "country": ["india", "australia", "uae", "brazil", "canada"],
}

def pick_word():
    category = random.choice(list(WORDS.keys()))
    word = random.choice(WORDS[category])
    return category, word

def display_state(word, guessed, attempts_left):
    print(HANGMAN_PICS[len(HANGMAN_PICS) - 1 - attempts_left])
    hidden = " ".join([c if c in guessed else "_" for c in word])
    print("Word:", hidden)
    print("Guessed letters:", " ".join(sorted(guessed)))
    print("Attempts left:", attempts_left)

def play():
    category, word = pick_word()
    attempts_left = len(HANGMAN_PICS) - 1
    guessed = set()
    print(f"Hint: Category is '{category}'.")
    while attempts_left > 0:
        display_state(word, guessed, attempts_left)
        guess = input("Guess a letter: ").strip().lower()
        if not guess or any(ch not in string.ascii_lowercase for ch in guess) or len(guess) != 1:
            print("Please enter a single alphabetic character.")
            continue
        if guess in guessed:
            print("Already guessed.")
            continue
        guessed.add(guess)
        if guess in word:
            print("Good guess!")
            if all(c in guessed for c in set(word)):
                print("You win! The word was:", word)
                return
        else:
            print("Wrong guess.")
            attempts_left -= 1
    display_state(word, guessed, attempts_left)
    print("You lost! The word was:", word)

if __name__ == "__main__":
    play()
