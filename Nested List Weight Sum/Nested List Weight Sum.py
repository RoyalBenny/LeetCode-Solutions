#Time: O(N)
#Space: O(D)
#list
def calculateSum(l,depth=1):
    sum = 0
    for i in l:
        if type(i)==type(1):
            sum+= i*depth
        else:
            sum+= calculateSum(i,depth+1)
    return sum


l1 = [[1,[2]],2,[3,4]]
l2 = []
l3 = [1,[2,[3,[4,[6]]]],6]
l4 = [[1,1],2,[1,1]]
l5 = [1,[4,[6]]]
print(calculateSum(l1))
print(calculateSum(l2))
print(calculateSum(l3))
print(calculateSum(l4))
print(calculateSum(l5))
