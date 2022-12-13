#Time : O(n*n!)
#Space: O(n*n!)
# recursion and dp
# https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        output.append([nums[0]])
        for i in nums[1:]:
            temp = output[:]
            output.clear()
            for j in temp:
                pos = 0
                while pos<=len(j):
                    output.append(j[:pos]+[i]+j[pos:])
                    pos+=1
        return output
