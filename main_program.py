import random
import tkinter as tk

class Game():
    def __init__(self, root):
        root.title("Rock, Paper, Scissors Game")

        # 3x3 grid
        mainframe = tk.Frame(root, padx=3, pady=3, bd=12)
        mainframe.grid(column=0, row=0, sticky='news')
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        rock_button = tk.Button(mainframe, text="Rock", command=self.rock, width=8, height=2)
        rock_button.grid(column=1, row=1, sticky='w')

        paper_button = tk.Button(mainframe, text="Paper", command=self.paper, width=8, height=2)
        paper_button.grid(column=1, row=2, sticky='w')

        scissors_button = tk.Button(mainframe, text="Scissors", command=self.scissors, width=8, height=2)
        scissors_button.grid(column=1, row=3, sticky='w')

        self.player_choice_label = tk.Label(mainframe, text="You chose: ", width=25, height=2)
        self.player_choice_label.grid(column=2, row=1, sticky='w')

        self.computer_choice_label = tk.Label(mainframe, text="The computer chose: ", width=25, height=2)
        self.computer_choice_label.grid(column=2, row=2, sticky='w')

        self.result_label = tk.Label(mainframe, text="Result: ", width=25, height=2)
        self.result_label.grid(column=2, row=3, sticky='w')

        self.wins = 0
        self.win_streak = tk.Label(mainframe, text="Wins: ", width=8, height=2)
        self.win_streak.grid(column=3, row=1)

        self.losses = 0
        self.loss_streak = tk.Label(mainframe, text="Losses: ", width=8, height=2)
        self.loss_streak.grid(column=3, row=2)

        self.ties = 0
        self.tie_streak = tk.Label(mainframe, text="Ties: ", width=8, height=2)
        self.tie_streak.grid(column=3, row=3)

    def rock(self) -> None:
        self.determine_winner("Rock")

    def paper(self) -> None:
        self.determine_winner("Paper")

    def scissors(self) -> None:
        self.determine_winner("Scissors")

    def determine_winner(self, user_choice) -> None:
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        self.player_choice_label.config(text=f"You chose: {user_choice}")
        self.computer_choice_label.config(text=f"The computer chose: {computer_choice}")

        if user_choice == computer_choice:
            self.result_label.config(text="Result: It's a tie!")
            self.ties += 1
            self.tie_streak.config(text=f"Ties: {self.ties}")

        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
                self.result_label.config(text="Result: You win!")
                self.wins += 1
                self.win_streak.config(text=f"Wins: {self.wins}")
        else:
            self.result_label.config(text="Result: Computer wins!")
            self.losses += 1
            self.loss_streak.config(text=f"Losses: {self.losses}")



root = tk.Tk()
root.geometry("380x150")
Game(root)
root.mainloop()
