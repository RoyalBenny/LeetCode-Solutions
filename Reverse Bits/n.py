#Time : O(n)
#Space: O(n)
# bit manipulation
def reverseBits(n: int) -> int:
        val = '0b'+ ('0'*(32-len(bin(n))+2)+(bin(n))[2:])[::-1]
        return int(val,2)
print(reverseBits(43261596))
