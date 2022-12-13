#Time: O(log(n))
#Space: O(1)
# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
def minBitFlips(start: int, goal: int) -> int:
        return bin(start ^ goal).count('1')
print(minBitFlips(14,1))
