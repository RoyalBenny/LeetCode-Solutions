#Dynamic Programming
#https://leetcode.com/problems/n-queens-ii/
class Solution:
    def __init__(self):
        self.count = 0
    def totalNQueens(self, n: int) -> List[List[str]]:
        self.nQueens(n,set(),set(),set())
        return self.count
    
    
    def nQueens(self,n,cols,posD,negD):
        if len(cols) == n:
            self.count+=1
            return
        row = len(cols)-1
        for i in range(n):
            if i in cols or row+i in posD or row-i in negD:
                continue
            cols.add(i)
            posD.add(row+i)
            negD.add(row-i)
            self.nQueens(n,cols,posD,negD)
            cols.remove(i)
            posD.remove(row+i)
            negD.remove(row-i)
    
    
        
        
