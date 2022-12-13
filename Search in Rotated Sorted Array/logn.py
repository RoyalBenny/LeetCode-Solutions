#Time : O(logN)
#Space: O(logN)
#searching
# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l = 0
        r=len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]==t:
                return mid
            if nums[l]<=nums[mid]:
                if nums[l]<=t<=nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<=t<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
            
        return l if nums[l] == t  else -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        return self.binarySearch(nums,0,len(nums)-1,target)
    
    def binarySearch(self,nums,start,end,target):
        if start>end:
            return -1
        mid = (start+end)//2
        if nums[mid] == target:
            return mid
        elif nums[start]> nums[mid] and target>=nums[start]:
            return self.binarySearch(nums,start,mid-1,target)
            
        elif nums[end]<nums[mid] and target<=nums[end]:
            return self.binarySearch(nums,mid+1,end,target)
            
        elif target>nums[mid]:
            return self.binarySearch(nums,mid+1,end,target)
            
        else:
            return self.binarySearch(nums,start,mid-1,target)
            
