# Time : O(n)
# Space : O(1)
# String
def isUnique(s):
    check = 0
    for i in s:
        bitValue = ord(i)
        if(check & (1<<bitValue) > 0):
            return False
        check |= (1<<bitValue)
    return True
print(isUnique("j?nfkdJCS!?"))
print(isUnique("abcd"))
print(isUnique(""))
