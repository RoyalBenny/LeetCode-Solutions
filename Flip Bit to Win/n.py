# Time : O(n)
# Space : O(1)
# Bit manipulation
def flip(num):
    if ~num == 0 : return len(bin(num))-2 if num  >=0 else len(bin(num))-3
    temp = 1
    num = abs(num)
    current = 0
    prev = 0
    result = 0
    while temp < num :
        if temp & num == 0:
            result= max(result,current+prev+1)
            prev = current
            current = 0
        else:
            current+=1
        temp = temp << 1
    return max(result,current+prev+1)

print(flip(100))
