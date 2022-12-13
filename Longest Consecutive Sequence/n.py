#Time : O(N)
#Space: O(N)
#array
# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        visited = set()
        maxLen = 1
        for i in nums:
            if i in visited:
                continue
            visited.add(i)
            count, temp = 1, i-1
            while temp in numSet:
                visited.add(temp)
                count+=1
                temp-=1
                
            temp = i+1
            while temp in numSet:
                visited.add(temp)
                count+=1
                temp+=1
            maxLen = max(count,maxLen)
        return maxLen
            
