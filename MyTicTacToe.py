def main():
    before_game()
    player, win, draw = in_game()
    post_game(player, win, draw)

def before_game(): 
    print("Welcome to Tic Tac Toe!")

def in_game():
    player = "O"
    win = False
    draw = False
    board = create_board()
    while not win and not draw:
        player = switch_player(player)
        print_board(board)
        player_turn(player, board)
        win = check_win(board, player)
        draw = check_draw(board)
    return player, win, draw
        
def create_board():
    board = [["N","N","N"], ["N","N","N"], ["N","N","N"]]
    return board

def player_turn(player, board):
    valid = False
    print(player + ", it is your turn.")
    while not valid: 
        row = int(input("Please enter the row number you want to play:"))
        col = int(input("Please enter the column number you want to play:"))
        valid = valid_move(board, row, col)
    update_board(player, board, row, col)
    return board

def valid_move(board, row, col):
    if board[row][col] == "N": 
        return True
    print()
    print()
    print()
    print("That position is already taken. Please input another move!")
    return False 

def update_board(player, board, row, col):
    board[row][col] = player
    return board

def check_win(board, player):
    winning_list = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
                     [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
                     [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
    for i in range(8):
        win = True
        for j in range(3): 
            row, col = winning_list[i][j]
            if board[row][col] != player: 
                win = False
                break
        if win: 
            return True
    return False

def check_draw(board): 
    for i in range(3): 
        for j in range(3): 
            if board[i][j] == "N":
                return False
    return True

def print_board(board):
    print()
    for i in range(3):
        line = []
        for j in range(3):
            if not board[i][j]:
                line.append("N")
            else: 
                line.append(board[i][j])
            line.append(" ")
        print("".join(line))
    print()

def switch_player(player):
    if player == "X":
        player = "O"
    else: 
        player = "X"
    return player

def post_game(player, win, draw):
    print()
    print()
    print()
    if win: 
        print("Congratulations player " + player + ", you've won!!!")
    else: 
        print("The game ended as a draw!")

if __name__ == "__main__":
    main()