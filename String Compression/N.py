#Time: O(N)
#Space: O(1)
#String
# https://leetcode.com/problems/string-compression/
def compress(chars) :
        if len(chars) == 1:
            return 1,chars
        i,count,pos = 1,1,1
        while i <len(chars):
            if chars[i] == chars[i-1]:
                count+=1
            else:
                pos = addToChars(chars,count,pos)
                chars[pos] = chars[i]
                count = 1
                pos+=1
            i+=1
        pos = addToChars(chars,count,pos)
        return pos,chars[:pos]
    
def addToChars(chars,count,pos):
        if count == 1:
            return pos
        for i in str(count):
            chars[pos] = i
            pos+=1
        return pos


print(compress(["a","a","b","b","c","c","c"]))
print(compress(["a"]))
print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
