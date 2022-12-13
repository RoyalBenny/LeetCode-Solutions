#T: O(N) S:(1)
class Solution:
    def climbStairs(self, n: int) -> int:
            a=1
            b=1
            while n:
                a,b = b,a+b
                n-=1
            return a

#Time : O(n)
#Space: O(1)
# https://leetcode.com/problems/climbing-stairs/
# Dymanic programming
def climbStairs(n: int) -> int:
        if n <= 2:
            return n
        a,b = 1,2
        for i in range(3,n+1):
            a,b = b,a+b
        return b

print(climbStairs(7))
