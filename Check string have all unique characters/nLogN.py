#Time : O(nlogn)
#Space: O(1)
#String
def isUnique(s):
    s = list(s)
    s.sort()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True

print(isUnique("aaabbccdaa"))
print(isUnique("abcd"))
print(isUnique(""))
