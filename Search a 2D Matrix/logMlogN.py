#Time: O(logM+logN)
#Space: O(1)
#Binary Search
#https://leetcode.com/problems/search-a-2d-matrix/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix)-1
        found = False
        index = -1
        
        while(start<=end):
            mid = (start+end)//2
            if matrix[mid][0]<=target and matrix[mid][-1]>=target:
                found = True
                index = mid
                break
            elif matrix[mid][0]>target:
                end = mid-1
            else:
                start = mid+1
        if not found:
            return False
        start = 0
        end = len(matrix[0])-1
        while(start<=end):
            mid = (start+end)//2
            if matrix[index][mid]==target:
                return True
            elif matrix[index][mid]>target:
                end = mid-1
            else:
                start = mid+1
        return False
