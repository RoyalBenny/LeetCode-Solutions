#T: O(N) S:O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup = 0
        for i in nums:
            if dup>dup^1<<i:
                return i
            dup^=1<<i

#Time: O(N)
#Space: O(1)
#Floyd's Cycle Detection Algorithm
#https://leetcode.com/problems/find-the-duplicate-number/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = nums[slow]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
        
        slow = 0
        
        while nums[fast]!= slow:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
