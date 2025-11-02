import random

class TicTacToe:
    def __init__(self, size=3):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.current_player = 'X'
        self.scores = {'X': 0, 'O': 0, 'Draw': 0}

    def print_board(self):
        for row in self.board:
            print(' | '.join(row))
            print('-' * (self.size * 4 - 1))

    def is_winner(self, player):
        # Check rows, columns, and diagonals
        for i in range(self.size):
            if all(self.board[i][j] == player for j in range(self.size)) or \
               all(self.board[j][i] == player for j in range(self.size)):
                return True
        if all(self.board[i][i] == player for i in range(self.size)) or \
           all(self.board[i][self.size - 1 - i] == player for i in range(self.size)):
            return True
        return False

    def is_full(self):
        return all(self.board[i][j] != ' ' for i in range(self.size) for j in range(self.size))

    def get_available_moves(self):
        return [(i, j) for i in range(self.size) for j in range(self.size) if self.board[i][j] == ' ']

    def minimax(self, depth, is_maximizing):
        if self.is_winner('O'):
            return 10 - depth
        if self.is_winner('X'):
            return depth - 10
        if self.is_full():
            return 0

        if is_maximizing:
            best = -float('inf')
            for move in self.get_available_moves():
                self.board[move[0]][move[1]] = 'O'
                best = max(best, self.minimax(depth + 1, False))
                self.board[move[0]][move[1]] = ' '
            return best
        else:
            best = float('inf')
            for move in self.get_available_moves():
                self.board[move[0]][move[1]] = 'X'
                best = min(best, self.minimax(depth + 1, True))
                self.board[move[0]][move[1]] = ' '
            return best

    def best_move(self):
        best_val = -float('inf')
        best_move = None
        for move in self.get_available_moves():
            self.board[move[0]][move[1]] = 'O'
            move_val = self.minimax(0, False)
            self.board[move[0]][move[1]] = ' '
            if move_val > best_val:
                best_val = move_val
                best_move = move
        return best_move

    def play(self):
        while True:
            self.board = [[' ' for _ in range(self.size)] for _ in range(self.size)]
            self.current_player = 'X'
            game_over = False

            while not game_over:
                self.print_board()
                if self.current_player == 'X':
                    try:
                        row = int(input(f"Player {self.current_player}, enter row (0-{self.size-1}): "))
                        col = int(input(f"Player {self.current_player}, enter col (0-{self.size-1}): "))
                        if self.board[row][col] == ' ':
                            self.board[row][col] = self.current_player
                        else:
                            print("Invalid move. Try again.")
                            continue
                    except (ValueError, IndexError):
                        print("Invalid input. Try again.")
                        continue
                else:
                    print("AI is thinking...")
                    move = self.best_move()
                    self.board[move[0]][move[1]] = 'O'

                if self.is_winner(self.current_player):
                    self.print_board()
                    print(f"{self.current_player} wins!")
                    self.scores[self.current_player] += 1
                    game_over = True
                elif self.is_full():
                    self.print_board()
                    print("It's a draw!")
                    self.scores['Draw'] += 1
                    game_over = True
                else:
                    self.current_player = 'O' if self.current_player == 'X' else 'X'

            print(f"Scores: X: {self.scores['X']}, O: {self.scores['O']}, Draws: {self.scores['Draw']}")
            play_again = input("Play again? (y/n): ").lower()
            if play_again != 'y':
                break

if __name__ == "__main__":
    size = int(input("Enter board size (e.g., 3 for standard): "))
    game = TicTacToe(size)
    game.play()