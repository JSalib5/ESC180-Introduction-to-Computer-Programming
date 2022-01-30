
import random

def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3)
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")

def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
#Part 1a
def placement_function(square_num):
    coord = [((square_num - 1) // 3), (square_num - 1) % 3] 
    return coord

#Part 1b
def put_in_board(board, mark, square_num):
    coord = placement_function(square_num)
    board[coord[0]][coord[1]] = mark
    return board

#Part 2a 
def get_free_squares(board):
    empty_squares = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_squares.append([i, j])
    return empty_squares

#Part 2b
def make_random_move(board, mark):
    i = 0
    row_random = 0
    column_random = 0
    while i == 0:
        empty_squares = get_free_squares(board)
        row_random = int(3*random.random())
        column_random = int(3*random.random())
        if [row_random, column_random] in empty_squares:
            board[row_random][column_random] = mark
            i += 1
    return board
#rand_coord=empty_squares[int(len(empty_squares)*random.random()))

#Part 3a
def is_row_all_marks(board, row_i, mark):
    for i in range(3):
        if board[row_i][i] != mark:
            return False
    return True
      
#Part 3b
def is_col_all_marks(board, col_i, mark):
    for i in range(3):
        if board[i][col_i] != mark:
            return False
    return True
        
#Part 3c
def is_win(board, mark):
    for i in range(3):
        if is_row_all_marks(board, i, mark) or is_col_all_marks(board, i, mark):
            return True
        if board[0][0] == board[1][1] == board[2][2] == mark or board[0][2] == board[1][1] == board[2][0] == mark:
            return True
    return False


#Part 4a and 4b
def computer_move():
    coord1 = []
    for k in range(len(get_free_squares(board))):
        L = get_free_squares(board)
        coord1 = L[k]
        board[coord1[0]][coord1[1]] = "O"
        if is_win(board, "O"):
            put_in_board(board, mark, int(input_str))
            
            return
        else:
            board[coord1[0]][coord1[1]] = " "
    make_random_move(board, "O")
    return

#part 4b
def check_rep(board, square_num):
    empty_squares = get_free_squares(board)
    coord = placement_function(square_num)
    if coord in empty_squares:
        return True
    else:
        return False

if __name__ == '__main__':
    count_choice = 0
    input_choice = input ("Play with Human or AI? ")
    
        
    if input_choice == "Human":
        print("\n\n")
        board = make_empty_board()
        print_board_and_legend(board)
        count = 0
        count1 = 0
        i = 0
        
        #Part 1c
        while i <= 9+count:
            print("\n\n")
            input_str = " "
            input_str = input ("Enter your move: ")
            if input_str == "end":
                break
            i += 1       
            while check_rep(board, int(input_str)) == False:
                count1 += 1
                print("The user chose an invalid space, {} times".format(count1))
                print("\n")
                input_str = input("Please choose a free space: ")
            while int(input_str) > 9 or int(input_str) < 1:
                count += 1
                print("The user did not choose from 1-9, {} times".format(count))
                print("\n")
                input_str = input("Please choose from 1 to 9: ")
                
            if i % 2 == 0 and i != 0:
                mark = "O"
            else:
                mark = "X"  
            
            print("\n\n")
            put_in_board(board, mark, int(input_str))
            print_board_and_legend(board)
            #Part 3d
            if is_win(board, mark):
                print(str(mark) + " Wins!")
                break
    
    if input_choice == "AI":
        mark = "X"
        print("\n\n")
        board = make_empty_board()
        print_board_and_legend(board)
        count = 0
        i = 0
        count1 = 0
        
        #Part 1c
        while i <= 9+count:
            print("\n\n")
            input_str = " "
            input_str = input ("Enter your move: ")
            if input_str == "end":
                break
            while check_rep(board, int(input_str)) == False:
                count1 += 1
                print("The user chose an invalid space, {} times".format(count1))
                print("\n")
                input_str = input("Please choose a free space: ")
                
            i += 1       

            while int(input_str) > 9 or int(input_str) < 1:
                count += 1
                print("The user did not choose from 1-9, {} times".format(count))
                print("\n")
                input_str = input("Please choose from 1 to 9: ")
            
            print("\n\n")
            put_in_board(board, mark, int(input_str))
            print_board_and_legend(board)
            #Part 3d
            if is_win(board, "X"):
                print("Player Wins!")
                break
            
            computer_move()
            print("\n\n")
            print_board_and_legend(board)
            if is_win(board, "O"):
                print("Computer Wins!")
                break
    

