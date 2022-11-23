#Time_Complexity: O(n)
#Space_Complexity: O(n) - Recursive stack space

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []    #Initialize result as an empty array
        self.backtrack(s, 0, [])    #Recursive function call with s, starting index as 0, and an emoty array which stores the partitions
        
        return self.result  #Return result
    
    
    
    def backtrack(self, s, pivot, path):    #Recursive function with s, pivot as the index, and path
        #base condition
        if pivot == len(s): #If the pivot is equal to the length of s then append a shallow copy of path into result and return which unfolds the recursion
            self.result.append(path[:])
            return
        
        #logic
        for i in range(pivot, len(s)):  #Continue till length of s
            subString = s[pivot:i+1]    #Build subString as partitioning s from the pivot index till i+1
            if self.isPalindrome(subString):    #Check if the subString is a palindrome or not, if yes append it to the path
                #action
                path.append(subString)
                
                #recurse
                self.backtrack(s, i+1, path)    #Recursive call by incrementing the index by 1
                
                #backtrack
                path.pop()  #Pop the element in to path where the last element is removed which is not choosen
    
    
    
    def isPalindrome(self, s):  #isPalindrome function to find whether the string is palindrome or not
        left = 0    #Initiaize ledt to 0
        right = len(s)-1    #Initialize right to the end of the string
        
        while left<right:   #Continue till left and right crosses each other
            if s[left] == s[right]: #If the s[left] is equal to s[right] then increment left by 1 and decrement right by 1
                left += 1
                right -= 1
                
            else:   #Else return false
                return False
        return True #Return true
    
    