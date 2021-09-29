def display_board(board):
    
    print(f'{board[1]}|{board[1]}|{board[2]}')
    print('-+-+-')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print('-+-+-')
    print(f'{board[6]}|{board[7]}|{board[8]}')


def create_board():
    '''
    Creates and returns a new board (list of strings)
    '''
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']



def get_user_choice():
    '''
    Asks the user for their choice of squares and return
    '''
    pass


def is_tie_game(board):
    '''

    '''
    pass


def is_game_over(board):
    '''
    Checks if the game is over because it's a win or tie.
    '''
    pass


def main():
    board = create_board()
    display_board(board)


if __name__ == '__main__':
    main()
