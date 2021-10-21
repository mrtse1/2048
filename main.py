from utilities import generate_piece, print_board

DEV_MODE = False
row = []

def main(game_board: [[int, ], ]) -> [[int, ], ]:
    new_piece = generate_piece(game_board, DEV_MODE)
    game_board[new_piece['row']][new_piece['column']] = new_piece["value"]
    user_turn = False
    computer_turn = True
    print_board(game_board)
    
    while True:
        if computer_turn == True:
            new_piece = generate_piece(game_board, DEV_MODE)
            game_board[new_piece['row']][new_piece['column']] = new_piece["value"]
            if game_over(game_board) == True:
                print_board(game_board)
                print('Game Over')
            computer_turn = False
            user_turn = True

        valid_inputs = ['w', 'a', 's', 'd', 'q']
        user_input = input()
        while user_input not in valid_inputs:
            user_input = input()
        if game_over(game_board):
            break

        if user_turn == True:
            computer_turn = True
            user_turn = False

        if user_input == 'd':
            for row in range(4):
                for column in range(1, 4):
                    if game_board[row][column] == 0:
                        game_board[row][column] = game_board[row][column - 1]
                        game_board[row][column - 1] = 0
            for row in range(4):
                for column in range(3, -1, -1):
                    if game_board[row][column - 1] == 0:
                        del game_board[row][column - 1]
            for row in range(4):
                while len(game_board[row]) <= 3:
                    game_board[row].insert(0, 0)
            for row in range(3, -1, -1):
                for column in range(3, 0, -1):
                    if game_board[row][column] == game_board[row][column - 1]:
                        game_board[row][column] = game_board[row][column] * 2
                        game_board[row][column - 1] = 0
            for row in range(4):
                for column in range(3, -1, -1):
                    if game_board[row][column - 1] == 0:
                        del game_board[row][column - 1]
            for row in range(4):
                while len(game_board[row]) <= 3:
                    game_board[row].insert(0, 0)

        elif user_input == 's':
            for column in range(3, -1, -1):
               for row in range(3, -1, -1):
                   for backwards in range(row - 1, -1, -1):
                       if game_board[row][column] == 0:
                           game_board[row][column] = game_board[backwards][column]
                           game_board[backwards][column] = 0
            for column in range(3, -1, -1):
                for row in range(3, -1, -1):
                    if game_board[row][column] == game_board[row - 1][column]:
                        game_board[row][column] *= 2
                        game_board[row - 1][column] = 0
            for column in range(3, -1, -1):
                for row in range(3, -1, -1):
                    for backwards in range(row - 1, -1, -1):
                        if game_board[row][column] == 0:
                            game_board[row][column] = game_board[backwards][column]
                            game_board[backwards][column] = 0


        elif user_input == 'w':
            for column in range(4):
               for row in range(3):
                   if game_board[row][column] == 0:
                       game_board[row][column] = game_board[row + 1][column]
                       game_board[row + 1][column] = 0
            for column in range(4):
                for row in range(3):
                    if game_board[row + 1][column] == game_board[row][column]:
                        game_board[row][column] *= 2
                        game_board[row + 1][column] = 0
            for column in range(4):
                for row in range(3):
                    if game_board[row][column] == 0:
                        game_board[row][column] = game_board[row + 1][column]
                        game_board[row + 1][column] = 0
            for column in range(4):
                for row in range(2):
                    if game_board[row + 1][column] == game_board[row + 2][column]:
                        game_board[row + 1][column] = game_board[row + 1][column] * 2
                        game_board[row + 2][column] = 0

        elif user_input == 'a':
            for row in range(len(game_board)):
                for column in range(3):
                    if game_board[row][column] == 0:
                        game_board[row][column] = game_board[row][column + 1]
                        game_board[row][column + 1] = 0
                for column in range(3):
                    if game_board[row][column + 1] == game_board[row][column]:
                        game_board[row][column] = game_board[row][column] * 2
                        game_board[row][column + 1] = 0
                for column in range(3, -1, -1):
                    if game_board[row][column] == 0:
                        del game_board[row][column]
                while len(game_board[row]) <= 3:
                    game_board[row].append(0)

        elif user_input == 'q':
            print("Goodbye")
            break

        if win(game_board):
            break
        print_board(game_board)
    return game_board

def win(game_board):
    for row in range(3):
        for column in range(3):
            if game_board[row][column] == 2048:
                return True
    return False


def game_over(game_board: [[int, ], ]) -> bool:
    for row in range(3):
        for column in range(3):
            if game_board[row][column] == game_board[row + 1][column] or game_board[row][column] == game_board[row][column + 1]:
                return False
    for row in range(4):
        for column in range(4):
            if game_board[row][column] == 0:
                return False
    else:
        return True

if __name__ == "__main__":
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])
