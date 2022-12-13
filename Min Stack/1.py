# Time : O(1)
# Space : O(n)
# Stack
#https://leetcode.com/problems/min-stack/
class Node:
    def __init__(self,val,min):
        self.val = val
        self.min = min
        

class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(Node(val,val))
        else:
            self.stack.append(Node(val,min(val,self.stack[-1].min)))
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop(-1)
        

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1].val
        return -1

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return float('Inf')
        return self.stack[-1].min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
