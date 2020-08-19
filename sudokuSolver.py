

board = [
    [7,8,0,4,0,0,1,2,0], #row 0
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
#recursive function, base case is a full board
def solve(board):

    find = find_empty(board)
    if not find:
        return True #board is full 
    else:
        row, col = find #returns next empty element on board
        
    for i in range(1,10):
        if valid(board, i, (row, col)):
            #if valid, add number to the board at valid pos
            board[row][col] = i
            
            #recursive call to board with newly added number
            if solve(board):
                return True:
            
            #if solve(board) with new number is not valid, this line of code
            #backtracks re-assigning the new number to 0
            board[row][col] = 0
            
    return False        

#check if board is valid
#ex pos 4, 3
def valid(board, num, pos):
    # pos = (row, col)
    row, col = pos
    # row = pos[0]
    # col = pos[1]
    
    #check row 0-8
    for i in range(len(board[0])):
        if board[row][i] == num and col != i:
        return False
    
    #check column 0-8
    for i in range(len(board)):
        if board[i][col] == num and row != i:
        return False

    #check box
    #ex. box_row = 3
    #ex. box_col = 2
    box_row = row // 3 #box_row = 1
    box_col = col // 3 #bow_col = 0
    
    for i in range(box_row * 3, box_row * 3 + 3): #ex range(3, 6)
        for j in range(box_col * 3, box_col * 3 + 3): #ex range(0, 3)
            #loops through each element in the box looking for a duplicate number
            if (board[i][j] == num and (i, j) != pos:
                return False
                
    #if the pos makes it to the end, it is a valid position
    return True
    
    
def print_board(board):
    
    for i in range(len(board)):
        #prints a dash line between every 3 rows
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
            
        #gets the length of the row    
        for j in range(len(board[0])):
            
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8:
                print(board[i][j])
            else:
            
#finds the next empty square on the board and returns its postion on the board            
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j) #returns row, column
    return None           

                
    

           