#Time : O(N**2)
#Time : O(N)
# Stack
#https://practice.geeksforgeeks.org/problems/sort-a-stack/1/#
class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self, s):
        # Code here
        if not s:
            return
        val = 0
        temp = []
        while s:
            val = s.pop(-1)
            while temp and temp[-1] < val:
                    s.append(temp.pop(-1))
            temp.append(val)
        while temp:
            s.append(temp.pop(-1))
