import tkinter as tk
from tkinter import messagebox

HUMAN = "X"
AI = "O"
EMPTY = " "

# ---------- Tic-Tac-Toe GUI ----------
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Tic-Tac-Toe (Unbeatable AI)")
        self.board = [EMPTY]*9
        self.buttons = []
        self.turn = HUMAN

        self.frame = tk.Frame(root, bg="#f0f0f0")
        self.frame.pack()

        # Title
        self.title_label = tk.Label(self.frame, text="Tic-Tac-Toe", font=("Arial", 20, "bold"), bg="#f0f0f0")
        self.title_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Create 3x3 board
        for i in range(9):
            btn = tk.Button(self.frame, text=" ", font=("Arial", 20, "bold"), width=5, height=2,
                            command=lambda i=i: self.make_move(i), bg="white", relief="raised")
            btn.grid(row=(i//3)+1, column=i%3, padx=5, pady=5, sticky="nsew")
            self.buttons.append(btn)

        # Reset button
        self.reset_button = tk.Button(self.frame, text="🔄 Reset", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", command=self.reset_game)
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=10)

    def make_move(self, idx):
        if self.board[idx] == EMPTY and self.turn == HUMAN:
            self.board[idx] = HUMAN
            self.update_button(idx)
            if self.check_winner(HUMAN):
                self.end_game("🎉 You win! (Well played!)")
            elif EMPTY not in self.board:
                self.end_game("It's a Draw 🤝")
            else:
                self.turn = AI
                self.ai_move()

    def ai_move(self):
        move = self.best_move()
        self.board[move] = AI
        self.update_button(move)
        if self.check_winner(AI):
            self.end_game("🤖 AI wins! Unbeatable for a reason.")
        elif EMPTY not in self.board:
            self.end_game("It's a Draw 🤝")
        else:
            self.turn = HUMAN

    def update_button(self, idx):
        mark = self.board[idx]
        color = "blue" if mark == HUMAN else "red"
        self.buttons[idx].config(text=mark, fg=color, relief="sunken")

    def check_winner(self, player):
        win_patterns = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for a,b,c in win_patterns:
            if self.board[a] == self.board[b] == self.board[c] == player:
                for i in (a,b,c):
                    self.buttons[i].config(bg="#90EE90")  # highlight green
                return True
        return False

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.reset_game()

    def reset_game(self):
        self.board = [EMPTY]*9
        for btn in self.buttons:
            btn.config(text=" ", bg="white", relief="raised")
        self.turn = HUMAN

    # Unbeatable AI using Minimax with Alpha-Beta Pruning
    def best_move(self):
        def minimax(board, maximizing, alpha, beta):
            win_patterns = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
            def winner(board):
                for a, b, c in win_patterns:
                    if board[a] != EMPTY and board[a] == board[b] == board[c]:
                        return board[a]
                return None
            win = winner(board)
            if win == AI:
                return 1, None
            if win == HUMAN:
                return -1, None
            if EMPTY not in board:
                return 0, None
            if maximizing:
                value = -float('inf')
                best = None
                for i in range(9):
                    if board[i] == EMPTY:
                        board[i] = AI
                        score, _ = minimax(board, False, alpha, beta)
                        board[i] = EMPTY
                        if score > value:
                            value = score
                            best = i
                        alpha = max(alpha, value)
                        if alpha >= beta:
                            break
                return value, best
            else:
                value = float('inf')
                best = None
                for i in range(9):
                    if board[i] == EMPTY:
                        board[i] = HUMAN
                        score, _ = minimax(board, True, alpha, beta)
                        board[i] = EMPTY
                        if score < value:
                            value = score
                            best = i
                        beta = min(beta, value)
                        if alpha >= beta:
                            break
                return value, best

        # Prefer center if available for speed
        if self.board[4] == EMPTY:
            return 4
        _, move = minimax(self.board[:], True, -float('inf'), float('inf'))
        return move if move is not None else [i for i in range(9) if self.board[i] == EMPTY][0]

# ---------- Run ----------
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
