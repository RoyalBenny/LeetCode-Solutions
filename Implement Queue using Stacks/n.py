#Time : O(n)
#Space: O(n)
# Stack and Queue
#https://leetcode.com/problems/implement-queue-using-stacks/
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.count = 0
        

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1
        if not self.stack2:
            self.rotate()
        self.count+=1
        return self.stack2.pop(-1)

    def peek(self) -> int:
        if not self.stack2:
            self.rotate()
        
        return self.stack2[-1]
        
    def empty(self) -> bool:
        return self.count == len(self.stack1)

    def rotate(self):
        self.stack2 = self.stack1[self.count:][::-1]
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
