#Time : O(N)
#Space: O(1)
# bitwise
# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/
class Solution:
    def greatestLetter(self, s: str) -> str:
        lower,higher = 0,0
        for i in s:
            if ord(i) >= ord('a'):
                lower |= 1<<(ord(i)-ord('a'))
            else:
                higher |= 1 <<(ord(i)-ord('A'))

        val = lower & higher
        if not val:
            return ''
        return chr(64+len(bin(val))-2)
