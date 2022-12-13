#Time : O(N*N!)
#Space: O(N*N!)
#recursion
# https://leetcode.com/problems/permutations-ii/
from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        dict = Counter(nums)
        output = []
        self.permute(len(nums),dict,[],output)
        return output
        
    def permute(self,n,uniqueNums,tempList,output):
        if len(tempList) == n:
            output.append(tempList[:])
            return
        for i in uniqueNums:
            if not uniqueNums[i]:
                continue
            tempList.append(i)
            uniqueNums[i]-=1
            self.permute(n,uniqueNums,tempList,output)
            uniqueNums[i]+=1
            tempList.pop(-1)
        
