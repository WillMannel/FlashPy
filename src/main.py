import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class FlashcardGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard App")
        self.flashcards = []

        # Layout
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Buttons
        tk.Button(self.frame, text="Add Flashcard", command=self.add_flashcard).pack(fill='x')
        tk.Button(self.frame, text="Show Flashcards", command=self.show_flashcards).pack(fill='x')
        tk.Button(self.frame, text="Quiz Me", command=self.quiz_me).pack(fill='x')
        tk.Button(self.frame, text="Exit", command=self.root.quit).pack(fill='x')

    def add_flashcard(self):
        question = simpledialog.askstring("Question", "Enter the question:")
        answer = simpledialog.askstring("Answer", "Enter the answer:")
        if question and answer:
            self.flashcards.append({'question': question, 'answer': answer})
            messagebox.showinfo("Success", "Flashcard added!")

    def show_flashcards(self):
        if not self.flashcards:
            messagebox.showinfo("Empty", "No flashcards to show. Please add some first.")
            return
        display = ""
        for i, card in enumerate(self.flashcards):
            display += f"Card {i+1}: Question: {card['question']} - Answer: {card['answer']}\n"
        messagebox.showinfo("Flashcards", display)

    def quiz_me(self):
        if not self.flashcards:
            messagebox.showinfo("Empty", "No flashcards to quiz. Please add some first.")
            return
        card = random.choice(self.flashcards)
        user_answer = simpledialog.askstring("Quiz", f"Question: {card['question']}")
        if user_answer.lower().strip() == card['answer'].lower().strip():
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Wrong! The correct answer was: {card['answer']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardGUI(root)
    root.mainloop()
