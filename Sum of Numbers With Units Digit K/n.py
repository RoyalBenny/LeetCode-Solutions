#Time :O(1)
#Space : O(1)
# math
# https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if not num:
            return 0
        for i in range(1,11):
            if i*k <= num and (num- i*k)%10 == 0:
                return i
        return -1
            
