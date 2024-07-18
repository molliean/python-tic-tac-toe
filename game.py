

print('Python Tic Tac Toe >:)')

# print current board
# print whose turn

class Game():
    def __init__(self, board, turn='x', tie=False, winner=None):
        self.turn = turn
        self.board = board
        self.tie = tie
        self.winner = winner
    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
            """)
    def print_message(self):
        if self.tie == True:
            print("Tie game!")
        elif self.winner != None:
            print(f"{self.winner} wins!")
        else:
            print(f"It's player {self.turn}'s turn.")
    def make_move(self):
        move = input(f"Enter a valid movie (example: A1): ").lower()
        valid_moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
        while True:
            print(move)
            if move in valid_moves and 
            # If the input is valid, update the board and break the loop
            # otherwise, print a message notifying the user of the invalid input and allow the loop to continue


# first_game = Game("")