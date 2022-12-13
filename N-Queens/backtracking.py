#Dynamic Programming
# https://leetcode.com/problems/n-queens/
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result =[]
        self.nQueens(n,set(),set(),set(),list(),result)
        return result
    
    def addOutput(self,result,cols,n):
        temp = []
        for i in cols:
            temp.append("."*i+"Q"+"."*(n-i-1))
        result.append(temp)
    
    def nQueens(self,n,cols,posD,negD,colList,result):
        if len(cols) == n:
            self.addOutput(result,colList,n)
            return
        row = len(cols)-1
        for i in range(n):
            if i in cols or row+i in posD or row-i in negD:
                continue
            cols.add(i)
            posD.add(row+i)
            negD.add(row-i)
            colList.append(i)
            self.nQueens(n,cols,posD,negD,colList,result)
            cols.remove(i)
            colList.pop(-1)
            posD.remove(row+i)
            negD.remove(row-i)
    
    
        
        
