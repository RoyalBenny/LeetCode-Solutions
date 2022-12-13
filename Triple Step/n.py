#Time : O(n)
#Space : O(n)
def tripleStep(n):
    if n <=2:
        return n
    output = [1,2,4]
    for i in range(4,n+1):
        output.append(output[-1]+output[-2]+output[-3])
    return output[-1]
print(tripleStep(8))
