import random

def main(): 
    before_game()
    player, win, draw = in_game()
    post_game(player, win, draw)

def before_game(): 
    print("Welcome to Tic Tac Toe!")

def first_player():
    if random.randint(1,2) == 1: 
        return "Computer"
    else: 
        return "User"

def in_game():
    current_player = first_player()
    player = "O"
    win = False
    draw = False
    board = create_board()
    possible_moves = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    while not win and not draw:
        current_player, player = switch_player(current_player, player)
        print_board(board)
        selection(current_player, player, board, possible_moves)
        win = check_win(board, player)
        draw = check_draw(board)
    print_board(board)
    return player, win, draw

def selection(current_player, player, board, possible_moves):
    selection = None
    if current_player == "User":
        while True:
            row = int(input("Please enter the row number you want to play:"))
            col = int(input("Please enter the column number you want to play:"))
            if (row, col) in possible_moves:
                selection = possible_moves.index(((row, col)))
                break
            print()
            print()
            print("Choose a valid move.")
            print()
            print()
    else:
        selection = random.randint(0, len(possible_moves) - 1)
    row, col = possible_moves.pop(selection)
    update_board(player, board, row, col)
    return board

def switch_player(current_player, player):
    if player == "X":
        player = "O"
    else: 
        player = "X"
    if current_player == "User": 
        current_player = "Computer"
    else: 
        current_player = "User"

    return (current_player, player)

def create_board():
    board = [["N","N","N"], ["N","N","N"], ["N","N","N"]]
    return board

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