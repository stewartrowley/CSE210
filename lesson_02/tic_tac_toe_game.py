

def board_move(game_board):
    '''
    This function controls the board move. Where you decide to go on the baord 
    and what you choose to end up doing. It will append your choice.
    '''

    board_number = []

    for key in game_board:
        board_number.append(key)


def board(game_board):
    '''
    This makes the game baord outline. The design of the board and 
    where you want  to go into the game. The design of the board
    is the main point.
    '''
    print(game_board['1'] + '|' + game_board['2'] + '|' + game_board['3'])
    print('-+-+-')
    print(game_board['4'] + '|' + game_board['5'] + '|' + game_board['6'])
    print('-+-+-')
    print(game_board['7'] + '|' + game_board['8'] + '|' + game_board['9'])


def game(game_board):
    '''
    This function does alot of the game. I honestly could of broken this part into more functions
    it does who turn it is and decides if you have won the game. 
    It does the main part of the function.
    '''

    turn = 'X'
    count = 0

    for i in range(10):
        board(game_board)
        print(
            f'It"s {turn} turn, where are you going to move?(type a number 1-9)')

        move = input()

        if game_board[move] == ' ':
            game_board[move] = turn
            count += 1
        else:
            print('That place is already filled. Move to a different spot.')
            continue

        if count >= 5:
            if game_board['7'] == game_board['8'] == game_board['9'] != ' ':
                board(game_board)
                print('Game Over!!!')
                print(f'{turn} won!!!')
                break
            elif game_board['4'] == game_board['5'] == game_board['6'] != ' ':
                print('Game Over!!!')
                print(f'{turn} won!!!')
                break
            elif game_board['1'] == game_board['2'] == game_board['3'] != ' ':
                board(game_board)
                print('Game Over!!!')
                print(f'{turn} won!!!')
                break
            elif game_board['1'] == game_board['4'] == game_board['7'] != ' ':
                board(game_board)
                print('Game Over!!!')
                print(f'{turn} won!!!')
                break
            elif game_board['2'] == game_board['5'] == game_board['8'] != ' ':
                board(game_board)
                print('Game Over!!!')
                print(f'{turn} won!!!')
                break
            elif game_board['3'] == game_board['6'] == game_board['9'] != ' ':
                board(game_board)
                print('Game Over!!!')
                print(f'{turn} won!!!')
                break
            elif game_board['7'] == game_board['5'] == game_board['3'] != ' ':
                board(game_board)
                print('Game Over!!!')
                print(f'{turn} won!!!')
                break
            elif game_board['1'] == game_board['5'] == game_board['9'] != ' ':
                board(game_board)
                print('Game Over!!!')
                print(f'{turn} won!!!')
                break

        if count == 9:
            print('Game Over!!!')
            print("It's a Tie!!")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


def main():
    '''
    This is the main function. it brings all of the functions together. 
    It calls all of the functions.
    '''
    board_direction = game_board = {'7': ' ', '8': ' ', '9': ' ',
                                    '4': ' ', '5': ' ', '6': ' ',
                                    '1': ' ', '2': ' ', '3': ' '}

    board_move(board_direction)

    game(board_direction)


if __name__ == "__main__":
    main()
