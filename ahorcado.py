from pyswip import Prolog
import tkinter as tk
from tkinter import messagebox

prolog = Prolog()
prolog.consult("ahorcado.pl")  # Reemplaza con la ruta a tu archivo Prolog

class JuegoAdivinanza:
    def __init__(self, master):
        self.master = master
        master.title("Juego de Adivinanza")

        self.word_label = tk.Label(master, text="")
        self.word_label.pack()

        # self.guess_entry = tk.Entry(master)
        # self.guess_entry.pack()

        # self.guess_button = tk.Button(master, text="Adivinar", command=self.guess_letter)
        # self.guess_button.pack()

        self.start_game()

    def start_game(self):

        

    # def guess_letter(self):
    #     guess = self.guess_entry.get().lower()

    #     if len(guess) == 1 and guess.isalpha():
    #         result = list(prolog.query(f"guess(Word, {self.guessed_letters + [guess]})."))[0]
    #         self.guessed_letters = result['GuessedLetters']
    #         self.word = result['Word']

    #         self.update_display()

    #         if '_' not in self.display_word():
    #             self.show_congratulations()
    #             self.start_game()
    #     else:
    #         messagebox.showerror("Error", "Ingresa una sola letra válida.")

    # def update_display(self):
    #     self.word_label.config(text=self.display_word())

    # def display_word(self):
    #     return ' '.join(letter if letter in self.guessed_letters else '_' for letter in self.word)

    # def show_congratulations(self):
    #     messagebox.showinfo("¡Felicidades!", f"¡La palabra es {''.join(self.word)}!")

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoAdivinanza(root)
    root.mainloop()
