import tkinter as tk
from pyswip import Prolog

class JuegoAhorcado:
    def __init__(self, master):
        self.master = master
        master.title("Ahorcado")

        self.prolog = Prolog()
        self.prolog.consult('ahorcado.pl')
        
        self.guessed_letters = []
        self.in_mind_result = list(self.prolog.query('in_mind(Word).'))
        self.word_in_mind_atoms = self.in_mind_result[0]['Word']
        self.word_in_mind = ''.join(str(atom) for atom in self.word_in_mind_atoms)
        self.left_words = [c for c in self.word_in_mind]
        self.word = self.left_words

        self.word_label = tk.Label(master, text="Palabra: ")
        self.word_label.pack()

        self.issue_text = tk.StringVar()
        self.issue_word_label = tk.Label(master, textvariable=self.issue_text)

        self.hits = 0

        self.label_imagen = tk.Label(master)
        self.label_imagen.pack()

        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack()

        self.update_display()

        self.guess_button = tk.Button(master, text="Adivinar", command=self.guess_letter)
        self.guess_button.pack()

        # Mostrar el estado inicial del ahorcado
        self.mostrar_estado_ahorcado()

    def start_game(self):
        result = list(self.prolog.query('in_mind(Word).'))[0]
        self.word = result['Word']
        self.guessed_letters = []
        self.hits = 0
        self.update_display()

    def guess_letter(self):
        guess = self.guess_entry.get().lower()
        print(f'Letra introducida: {guess}')

        is_in_word = bool(list(self.prolog.query(f'guess({self.left_words},{guess})')))
        print(is_in_word)
        print(self.in_mind_result)

        if is_in_word:
            self.left_words = [c for c in self.left_words if c != guess]
            print(self.left_words)
            self.guessed_letters.append(guess)
            self.update_display()
        elif bool(list(self.prolog.query(f'guess({self.guessed_letters},{guess})'))):
            self.show_repeat_letter(guess)
        else:
            self.wrong_letter(guess)
            self.hits += 1
            self.mostrar_estado_ahorcado()

        self.guess_entry.delete(0, tk.END)

        if not self.left_words:
            self.show_congratulations()

        if self.hits > 4:
            self.game_over()

    def update_display(self):
        self.word_label.config(text=f"Palabra: {self.display_word()}")

    def display_word(self):
        return ' '.join(letter if letter in self.guessed_letters else '_' for letter in self.word)

    def show_congratulations(self):
        self.issue_text.set(f"¡Felicidades! La palabra es {''.join(self.word)}")
        self.issue_word_label.pack()
        self.guess_entry.destroy()
        self.guess_button.destroy()

    def show_repeat_letter(self, guess):
        self.issue_text.set(f"¡Ya has acertado la letra {''.join(guess)}!")
        self.issue_word_label.pack()

    def mostrar_estado_ahorcado(self):
        estado_ahorcado = [
            "  -----\n |     |\n |     \n |     \n |     \n |     \n-",
            "  -----\n |     |\n |     O\n |     \n |     \n |     \n-",
            "  -----\n |     |\n |     O\n |     |\n |     \n |     \n-",
            "  -----\n |     |\n |     O\n |    /|\ \n |     \n |     \n-",
            "  -----\n |     |\n |     O\n |    /|\ \n |    / \ \n |     \n-"
        ]

        self.label_imagen.config(text=estado_ahorcado[self.hits])
        self.label_imagen.pack()

    def wrong_letter(self, guess):
        self.issue_text.set(f"No está la letra {''.join(guess)}!")
        self.issue_word_label.pack()

    def game_over(self):
        self.issue_text.set("¡Has perdido! La palabra era {}".format(''.join(self.word)))
        self.issue_word_label.pack()
        self.guess_entry.destroy()
        self.guess_button.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoAhorcado(root)
    root.mainloop()
