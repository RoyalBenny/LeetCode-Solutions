#Time: O((4^N)/sqrt(N))
#Space: O((4^N)/sqrt(N))
#Recursion, backtracking
# https://leetcode.com/problems/generate-parentheses/solution/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        self.generate("",n,n,output)
        return output
    
    def generate(self,paras,openCount,closeCount,output):
        if not openCount and not closeCount:
            output.append(paras)
            return
        if openCount:
            self.generate(paras+'(',openCount-1,closeCount,output)
        if closeCount > openCount:
            self.generate(paras+')',openCount,closeCount-1,output)
        
