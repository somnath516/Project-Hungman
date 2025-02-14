import random

# Constants for word lists, hangman graphics, and max guesses
WORD_LIST = {
    'easy': ['cat', 'dog', 'fish', 'bird'],
    'medium': ['python', 'computer', 'keyboard'],
    'hard': ['algorithm', 'exponential', 'cryptography']
}

HANGMAN_GRAPHICS = [
    '''
     -----
     |   |
         |
         |
         |
         |
    ========
    ''',
    '''
     -----
     |   |
     O   |
         |
         |
         |
    ========
    ''',
    '''
     -----
     |   |
     O   |
     |   |
         |
         |
    ========
    ''',
    '''
     -----
     |   |
     O   |
    /|   |
         |
         |
    ========
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    ========
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    ========
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========
    '''
]

MAX_INCORRECT = {'easy': 6, 'medium': 5, 'hard': 4}

def select_level():
    return random.choice(['easy', 'medium', 'hard'])

def get_word(level):
    return random.choice(WORD_LIST[level])

def display_word(word, guesses):
    return ' '.join([l if l in guesses else '_' for l in word])

def hangman_graphic(incorrect_guesses):
    return HANGMAN_GRAPHICS[min(incorrect_guesses, len(HANGMAN_GRAPHICS) - 1)]

def print_state(word, guesses, incorrect_guesses, level):
    print(hangman_graphic(incorrect_guesses))
    print(f"Word: {display_word(word, guesses)}")
    print(f"Remaining Chances: {'❤️ ' * (MAX_INCORRECT[level] - incorrect_guesses)}")

def play_game():
    level = select_level()
    word = get_word(level)
    guessed_letters, incorrect_guesses = [], 0

    while incorrect_guesses < MAX_INCORRECT[level]:
        print_state(word, guessed_letters, incorrect_guesses, level)
        guess = input("Guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha() and guess not in guessed_letters:
            guessed_letters.append(guess)
            if guess not in word: incorrect_guesses += 1
            if set(word).issubset(guessed_letters):
                print(f"Congrats! You guessed the word: {word}")
                break
        else:
            print("Invalid or repeated guess.")
    else:
        print(f"Game Over! The word was: {word}")
        print(hangman_graphic(incorrect_guesses))

if __name__ == "__main__":
    play_game()