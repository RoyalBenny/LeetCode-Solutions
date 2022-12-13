# Time : O(s2)
# Space : O(1)
def checkInclusion(s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        array1 = [0]*26
        array2 = [0]*26
        for i in s1:
            array1[ord(i)-ord('a')]+=1
        for i in s2[0:len(s1)]:
            array2[ord(i)-ord('a')]+=1
        if match(array1,array2):
            return True
        for i in range(len(s1),len(s2)):
            index = ord(s2[i-len(s1)]) - ord('a')
            array2[index] = 0 if array2[index] == 0 else array2[index]-1 
            array2[ord(s2[i])-ord('a')]+=1
            if match(array1,array2):
                return True
        return False
    
def match(a1,a2):
    for i in range(len(a1)):
        if a1[i] != a2[i]:
            return False
    return True

print(checkInclusion("ab","eidboaoo"))
print(checkInclusion("ab","eidbaoo"))
