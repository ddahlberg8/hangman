from re import X
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range (3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    # board = 0 | 1 | 2
    #         3 | 4 | 5
    #         6 | 7 | 8   

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # This one line above summarizes this entire for loop into 1 line
        # moves = []
        # for (i,spot) in enumerate(self.board):
        #     # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_spaces(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        #if valid move, then make the move by assigning a square to a letter
        #return false if move is invalid
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        #winner if 3 in a row anywhere
        #start with the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        #check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        #check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #left to right diagonal
            if all([spot == letter for spot in diagonal2]):
                return True


def play(game, x_player, o_player, print_game=True):
    #returns the winner of the game or None if there is no winner
    if print_game:
        game.print_board_nums()

    letter = 'X' #starting letter
    #iterate while the game still has empty sqares, but maybe I can change this as a little challenge for myself
    #when there is a winner the loop will break but this could be helpful for CAT games
    while game.empty_squares():
        #get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' make a move to square {square}')
                game.print_board()
                print('') #empty line
            
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X' #switches players
            # This line above surmizes the for loop down below and condenses it into 1 line
            # if letter = 'X':
            #     letter = 'O'
            # else:
            #     letter = 'X'
    if print_game:
        print("It's a tie")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)



#The user will have to take turns placing an X or and O and specify which position their letter is going to go
#We will have to take that input and save it to the new board and print the new board
#We will need to specify winning conditions or when there is no possible moves left and end the game
    #Maybe we could have the computer know when winning is no longer possible and stop the game when it is no longer possible to win instead of when there are no more moves
#Print out the winner
#Keep track of how many wins a player has
