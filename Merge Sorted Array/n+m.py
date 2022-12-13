#Time : O(n+m)
#Space : O(m)
# https://leetcode.com/problems/merge-sorted-array/
# Sorting
def merge(nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m]
        i,j,k=0,0,0
        while i<m and j <n:
            if temp[i]<nums2[j]:
                nums1[k] = temp[i]
                i+=1
            else:
                nums1[k] = nums2[j]
                j+=1
            k+=1
        for i in temp[i:]:
            nums1[k] = i
            k+=1
        for j in nums2[j:]:
            nums1[k] = j
            k+=1
        

array1 = [1,2,3,0,0,0]
m = 3
array2 = [2,5,6]
n =3
merge(array1,m,array2,n)
print(array1)
