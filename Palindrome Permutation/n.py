#Time: O(N)
#Space: O(1)
#String
import math
def PalindromePermuation(string):
    string = string.lower()
    s=0
    for i in string:
        if i != ' ':
            s^= 1<<(ord(i)-ord('a'))
    if s==0 or math.log(s,2) == round(math.log(s,2)):
        return True
    return False

print(PalindromePermuation("tact coq"))
print(PalindromePermuation("tact coa"))
print(PalindromePermuation(""))
print(PalindromePermuation("malayalam malayalam"))
print(PalindromePermuation("GeeksForgeeks"))
