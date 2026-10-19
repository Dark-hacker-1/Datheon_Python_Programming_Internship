import random

# ASCII Art for gallows stages (0 to 6 mistakes)
HANGMAN_PICS = [
    "  +---+\n      |\n      |\n      |\n     ===",
    "  +---+\n  O   |\n      |\n      |\n     ===",
    "  +---+\n  O   |\n  |   |\n      |\n     ===",
    "  +---+\n  O   |\n /|   |\n      |\n     ===",
    "  +---+\n  O   |\n /|\\  |\n      |\n     ===",
    "  +---+\n  O   |\n /|\\  |\n /    |\n     ===",
    "  +---+\n  O   |\n /|\\  |\n / \\  |\n     ==="
]

# Word list for the game
WORD_LIST = ["python", "developer", "internship", "datheon", "automation", "security", "programming", "repository"]

def get_random_word(word_list):
    return random.choice(word_list).upper()

def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()
    
    print("Missed letters:", end=" ")
    for letter in missed_letters:
        print(letter, end=" ")
    print()
    
    blank_word = ""
    for letter in secret_word:
        if letter in correct_letters:
            blank_word += letter + " "
        else:
            blank_word += "_ "
            
    print("Word:", blank_word)
    print()

def get_guess(already_guessed):
    while True:
        guess = input("Guess a letter: ").upper()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in already_guessed:
            print("You have already guessed that letter. Choose again.")
        elif not guess.isalpha():
            print("Please enter an alphabetical letter.")
        else:
            return guess

def play_game():
    print("=" * 40)
    print("WELCOME TO HANGMAN - DATHEON INTERNSHIP")
    print("=" * 40)
    
    secret_word = get_random_word(WORD_LIST)
    missed_letters = ""
    correct_letters = ""
    game_is_done = False

    while not game_is_done:
        display_board(missed_letters, correct_letters, secret_word)
        
        guess = get_guess(missed_letters + correct_letters)
        
        if guess in secret_word:
            correct_letters = correct_letters + guess
            
            found_all_letters = True
            for i in range(len(secret_word)):
                if secret_word[i] not in correct_letters:
                    found_all_letters = False
                    break
            if found_all_letters:
                print(f"\nYes! The secret word is '{secret_word}'! You have won!")
                game_is_done = True
        else:
            missed_letters = missed_letters + guess
            
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                display_board(missed_letters, correct_letters, secret_word)
                print(f"Out of moves!\nAfter {len(missed_letters)} missed guesses, the word was '{secret_word}'.")
                game_is_done = True

if __name__ == "__main__":
    while True:
        play_game()
        if input("Do you want to play again? (yes/no): ").lower().startswith('y'):
            continue
        else:
            print("Thank you for playing!")
            break
