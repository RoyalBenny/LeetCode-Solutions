#Time : O(N)
#Space:O(1)
#sorting
#https://leetcode.com/problems/first-missing-positive/submissions/
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        index = 0
        while index<len(nums):
            if self.isSwapable(nums,index):
                nums[nums[index]-1], nums[index] = nums[index], nums[nums[index]-1]
            else:
                index+=1
        for i in range(len(nums)):
            if (i+1)!=nums[i]:
                return i+1
        return len(nums)+1
    
    def isSwapable(self,nums,index):
        return nums[index]>0 and nums[index]<=len(nums) and
        nums[index]!=index+1 and nums[index]!=nums[nums[index]-1]
