#Time_Complexity: O(n)
#Space_Complexity: O(n) - Building the board

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[False for i in range(n)] for j in range(n)]   #Build the board by assigning False for all spaces
        self.result = []    #Initialize result as an empty array
        self.backtrack(board, 0)    #Recursive function call

        return self.result  #Return result
    
    
    def backtrack(self, board, r):  #Recursive function with board and row
        #base condtion
        if r == len(board): #If r is equal to len(board) then
            row = []    #Initialize row as an empty array
            for i in range(len(board)): #Continue till length of board
                stringBuild = ""    #Initialize stringBuild as an empty string
                for j in range(len(board)): #Continue till lenght of board
                    if board[i][j]: #If board[i][j] is True then add "Q" into the stringBuild
                        stringBuild += "Q"
                    else:   #Else add "." into the stringBuild
                        stringBuild += "."
                        
                row.append(stringBuild) #Append the stringBuild into row
            self.result.append(row) #Append the row into result 
            return  #Return and this will unfold the recursion
            
        #Logic 
        for c in range(len(board)): #Continue the columns till lenght of board
            if self.isSafe(board, r, c):    #If the row and column is safe to traverse
                board[r][c] = True  #Change board[r][c] as True
                
                self.backtrack(board, r+1)  #Recursive function call by incrementing row by 1 whihc means a Queen is placed in the previous row
            board[r][c] = False #Change board[r][c] to False to check the next row
            
            
            
            
            
            
    def isSafe(self, board, i, j):  #isSafe function returns whether it is safe to place the queen in that row and column or not
        for r in range(0, i):   #Continue till i
            if board[r][j]: #If board[i][j] is True then return False
                return False
        r = i   #Assign i to r  
        c = j   #Assign j to c
        #Left Diagonal
        while r >= 0 and c >= 0:    #Treaversing the left diagonal from r and c
            if board[r][c]: #If the board[r][c] is True then return False
                return False
            r -= 1  #Decrement r by 1
            c -= 1  #Decrement c by 1
            
        r = i   #Assign i to r
        c = j   #Assign j to c
        #Right Diagonal
        while r >= 0 and c < len(board):    #Traversing the right diagonal from r and c
            if board[r][c]: #If the board[r][c] is True then return False
                return False
            r -= 1  #Decrement r by 1
            c += 1  #Increment c by 1
            
        return True #If there is no true it is safe to place the queen so return True
        
        
        