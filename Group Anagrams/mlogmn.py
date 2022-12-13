#T: O(NM) S:O(N)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def countChars(word):
            counts = [0]*26
            for i in word:
                counts[ord(i)-97]+=1
            return tuple(counts)
        anagramDict = dict()
        output = []
        for st in strs:
            charCount = countChars(st)
            if charCount in anagramDict:
                output[anagramDict[charCount]].append(st)
            else:
                anagramDict[charCount] = len(output)
                output.append([st])
        return output

#Time : O(mlogm*n) - m= len(str)
#Space: O(N)
#sorting
#https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return
        anagD = dict()
        for str in strs:
            if str in anagD:
                anagD[str].append(str)
                continue
            sortedStr = "".join(sorted(str))
            if sortedStr in anagD:
                anagD[sortedStr].append(str)
            else:
                anagD[sortedStr] = [str]
        
        output = []
        for key in anagD:
            output.append(anagD[key])
        
        return output
