#Time: O(logN)
#Space: O(1)
#Searching
#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, arr: List[int]) -> int:
        l,r = 0 ,len(arr)-1
        while l<r:
            mid = (l+r)//2
            if arr[mid]<arr[r]:
                r=mid
            else:
                l=mid+1
        return arr[l]


class Solution:
    def findMin(self, arr: List[int]) -> int:
        start ,end = 0, len(arr)-1
        if arr[start]<=arr[end]:
            return arr[start]
        while(start<=end):
            mid = (start+end)//2
            if mid-1>-1 and arr[mid-1]>arr[mid]:
                return arr[mid]
            elif arr[mid]>arr[end]:
                start = mid+1
            else:
                end = mid-1
        return -1
                
