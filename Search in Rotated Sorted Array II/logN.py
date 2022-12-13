#Time: O(logN)
#Space: O(N)
#Searching
#https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        return self.binarySearch(nums,0,len(nums)-1,target)
    
    def binarySearch(self,nums,start,end,target):
        if start>end:
            return False
        mid = (start+end)//2
        if nums[mid] == target:
            return True
        
        elif start+1<=end and nums[start]== nums[start+1]:
            return self.binarySearch(nums,start+1,end,target)
        
        elif end-1>=start and nums[end] == nums[end-1]:
            return self.binarySearch(nums,start,end-1,target)
        
        elif nums[start]> nums[mid] and target>=nums[start]:
            return self.binarySearch(nums,start,mid-1,target)
            
        elif nums[end]<nums[mid] and target<=nums[end]:
            return self.binarySearch(nums,mid+1,end,target)
            
        elif target>nums[mid]:
            return self.binarySearch(nums,mid+1,end,target)
            
        else:
            return self.binarySearch(nums,start,mid-1,target)
            
