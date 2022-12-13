#Time : O(N*2^N)
#Space: O(2^N)
# Dynamic Programming
#https://leetcode.com/problems/subsets/
def subsets(nums):
        output = [[]]
        for i in nums:
            output.append([i])
        indexDict = {val:index for index,val in enumerate(nums)}
        i = 1
        while i <= len(output)-len(nums):
            last = output[i][-1]
            for j in nums[indexDict[last]+1:]:
                output.append(output[i]+[j])
            i+=1
        return output
print(subsets([1,2,3,4]))
