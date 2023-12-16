from pyswip import Prolog

# Inicializar el motor Prolog
prolog = Prolog()
prolog.consult("ahorcado.pl")  # Reemplaza con la ruta a tu archivo Prolog

def display_word(word, guessed_letters):
    displayed = [letter if letter in guessed_letters else '_' for letter in word]
    return ' '.join(displayed)

def start_game():
    prolog.query("start.")
    word = list(prolog.query("in_mind(Word), guess(Word, [])."))[0]['Word']
    guessed_letters = []

    while '_' in display_word(word, guessed_letters):
        print(display_word(word, guessed_letters))
        guess = input("Next letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            result = list(prolog.query(f"guess(Word, {guessed_letters + [guess]})."))[0]
            guessed_letters = result['GuessedLetters']
            remaining_word = result['Word']
        else:
            print("Invalid input. Please enter a single letter.")

    print(f"Congratulations! The word is {''.join(word)}")

if __name__ == "__main__":
    start_game()
