# Time : O(n)
# Space :O(1)
# Bit manipulation


def nextNumber(num):
    binary = 1
    large, small = [None,None]
    while (not large or not small) and num >= binary:
        if n| binary == n:
            if not large and n&(binary<<1)==0:
                large = (n ^ binary) | (binary <<1)
            if not small and n & (binary >> 1) == 0 and binary != 1:
                small = (n ^ binary) | (binary >>1)
        binary = binary << 1
    return [large, small]
n = 94511
print(nextNumber(n),bin(n))
