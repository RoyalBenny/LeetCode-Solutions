# Time : O(n)
# Space : O(1) because maxsize of this dict is 26
#string
from collections import Counter
def firstUniqueChar(s):
    count = Counter(s)
    for index, c in enumerate(s):
        if count[c] == 1:
            return index
    return -1

print(firstUniqueChar("leetcode"))
print(firstUniqueChar("loveleetcode"))
print(firstUniqueChar("abcdabc"))
