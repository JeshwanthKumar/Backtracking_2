#Time_Complexity: O(m*n)
#Space_Complexity: O(n) - Recursive stack space

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board= board   #Initialize board as board
        self.word = word    #Initialize word as word
        self.m = len(self.board)    #Initialize m as length of board
        self.n = len(self.board[0]) #Initialize n as length of columns
        
        #Edge case
        if len(self.word) > self.m*self.n:  #If the length of word is greater than m * n then return False
            return False
        
        self.dirs_= [[0,1],[0,-1],[1,0],[-1,0]] #Direction array
        
        for i in range(self.m): #Continue till m
            for j in range(self.n): #Continue till n
                if self.word[0] == self.board[i][j]:    #If the first letter in word is equal to the element in board
                    if self.dfs(i, j, 0):   #If the recursive funtion call is True return True
                        return True
                    
        return False    #Return False
    
    def dfs(self, i, j, index): #REcursive function with i and j as row and column and index as indices 
        #Base condition
        if index == len(self.word): #If the index is equal to length of word retun True
            return True
        
        if i < 0 or i == self.m or j < 0 or j == self.n or self.board[i][j] == '#': #If i less than 0 or equal to m or j is less than 0 or less than n or the element in board is '#' then return False
            return False
        
        if self.board[i][j] == self.word[index]:    #If the element in the board is equal to the element in word
            #action
            self.board[i][j] == '#' #Change the element in the board as '#'
            for x, y in self.dirs_: #For x an y in direction array
                nr = x+i    #Neighboring row as x+i
                nc = y+j    #Neighboring column as y+j
                #recurse
                if self.dfs(nr, nc, index+1):   #If the recursive function call by incrementing index by 1 is True then return True
                    return True
            #backtrack   
            self.board[i][j] = self.word[index] #Change the lsat element that is visited with the element in the word
                    
        return False    #Retrun False if no condition satisfies