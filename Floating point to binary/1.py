# Time : O(32) -> O(1)
# Space: O(1)
def binaryConverter(num):
    if num >= 1 or num <= 0:
        return "Error"
    binary = "."
    while num > 0:
        print(binary)
        if len(binary) > 32:
            return "Error"
        r = num * 2
        if r >= 1 :
            binary+=("1")
            num = r-1
        else:
            num = r
            binary+=("0")
    return binary

print(binaryConverter(0.55))
