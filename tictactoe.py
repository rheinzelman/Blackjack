class Board(object):
  def __init__(self):
    self.board = [["1","2","3"],["4","5","6"],["7","8","9"]]

  def print_board(self):
    print(' ', self.board[0][0], '|', self.board[0][1], '|', self.board[0][2])
    print('-------------')
    print(' ', self.board[1][0], '|', self.board[1][1], '|', self.board[1][2])
    print('-------------')
    print(' ', self.board[2][0], '|', self.board[2][1], '|', self.board[2][2])

  def mark_square(self, r, c, player):
    try:
      row = int(r)
      column = int(c)
    except ValueError:
      print("Sorry, that's not an acceptable input")
      return False
    if(self.board[row][column] == "X" or self.board[row][column] == "O"):
      print("Sorry, square already marked")
      return False
    elif((player != 'X' and player != "O")):
      print('Sorry, invalid Player')
      return False
    else:
      self.board[row][column] = player
      return True
        

  def has_winner(self):
    if (self.board[0][0] == self.board[0][1] == self.board[0][2]):
      return True
    elif (self.board[1][0] == self.board[1][1] == self.board[1][2]):
      return True
    elif (self.board[2][0] == self.board[2][1] == self.board[2][2]):
      return True
    elif (self.board[0][0] == self.board[1][0] == self.board[2][0]):
      return True
    elif (self.board[0][1] == self.board[1][1] == self.board[2][1]):
      return True
    elif (self.board[0][2] == self.board[1][2] == self.board[2][2]):
      return True
    elif (self.board[0][0] == self.board[1][1] == self.board[2][2]):
      return True
    elif (self.board[0][2] == self.board[1][1] == self.board[2][0]):
      return True
    else:
      return False

  def play_game(self):
    while(not self.has_winner()):
        userInput = input("Enter move: ")
          
        move = userInput.split(',')
          
        if(not len(move) == 3):
            print('Sorry, invalid input')
            continue
        else:
            self.mark_square(move[0], move[1],move[2])
            #print the board
            self.print_board()
    return move[2]

        
if __name__ == '__main__':
    board = Board()
    winner = board.play_game()
    print("{} has won!".format(winner))