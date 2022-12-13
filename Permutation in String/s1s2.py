# Time : O(s1*s2)
# Space : O(1)
# String
def checkInclusion( s1: str, s2: str) -> bool:
    if not s1 or not s2:
        return False
    s1Map = Counter(s1)
    s1Len = len(s1)
    copy = s1Map.copy()
    for i in range(len(s2)):
        j = i
        while j<len(s2) and s2[j] in copy and copy[s2[j]] > 0:
            copy[s2[j]]-=1
            s1Len-=1
            j+=1
            if s1Len == 0:
                return True
        if s1Len != len(s1):
            copy = s1Map.copy()
            s1Len = len(s1)
    return False
print(checkInclusion("ab","eidbaooo"))
print(checkInclusion("ab","eidboaooo"))
