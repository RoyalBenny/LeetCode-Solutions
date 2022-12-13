class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        rev = 0
        while(num>0):
            rev = rev*10+(num%10)
            num//=10
        if x>0 and rev> (2**31)-1:
            return 0
        if x<0 and rev>(2**31):
            return 0
        if x<0:
            return rev*-1
        return rev
