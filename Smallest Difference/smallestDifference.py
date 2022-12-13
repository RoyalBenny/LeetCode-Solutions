#Time: O(NlogN+ MlogM)
#Space: O(1)
#array
#https://www.geeksforgeeks.org/smallest-difference-pair-values-two-unsorted-arrays/
def smallestDiff(array1,array2):
    i,j=0,0
    array1.sort()
    array2.sort()
    min = float('Inf')
    while i < len(array1) and j< len(array2):
        diff = abs(array1[i]-array2[j])
        if  diff< min:
            min = diff
        if array1[i]< array2[j]:
            i+=1
        else:
            j+=1
    return min

array1 = [10,5,40]
array2 = [30,90,80]
print(smallestDiff(array1,array2))
