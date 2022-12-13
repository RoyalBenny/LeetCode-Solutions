#Time : O(2^N)
#Space: O(2^N)
# Dynamic Programming
#https://leetcode.com/problems/subsets/

def subsets(nums):
        output = []
        output.append([])
        for i in nums:
            temp=[]
            for j in output:
                temp.append(j+[i])
            output+=temp
        return output
print(subsets([1,2,3,4]))

#solution 2
#T: O(2^N) S: O(2^N)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerSet = [[]]
        for i in nums:
            for j in range(len(powerSet)):  
                powerSet.append(powerSet[j]+[i])
        return powerSet
