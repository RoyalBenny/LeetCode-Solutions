# Stack and queue
# https://leetcode.com/problems/dinner-plate-stacks/
from heapq import heappop,heappush
class DinnerPlates:

    def __init__(self, capacity: int):
        self.stack = []
        self.capacity = capacity
        self.heap = []
        

    def push(self, val: int) -> None:
        if not self.heap:
            self.addToStack(val)
            return
        index = heappop(self.heap)
        if index < len(self.stack):
            self.stack[index].append(val)
        else:
            self.addToStack(val)

    def pop(self) -> int:
        while self.stack and not self.stack[-1]:
            self.stack.pop(-1)
        if self.stack:
            return self.stack[-1].pop(-1)
        return -1

    def popAtStack(self, index: int) -> int:
        if index>=len(self.stack) or not self.stack[index]:
            return -1
        heappush(self.heap,index)
        return self.stack[index].pop(-1)
    
    def addToStack(self,val):
        if not self.stack or len(self.stack[-1]) >= self.capacity:
            self.stack.append([val])
        else:
            self.stack[-1].append(val)
        
        


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
