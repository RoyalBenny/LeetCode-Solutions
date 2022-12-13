#Time: O(1)
#Space: O(1)
#binary
#https://www.geeksforgeeks.org/compute-the-minimum-or-maximum-max-of-two-integers-without-branching/
def findMax(a,b):
    k = (b-a)>>31
    k&=1
    return (a*k)+(b*(not k))
print(findMax(10,17))
