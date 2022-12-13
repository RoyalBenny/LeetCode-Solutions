
def oneAway(s1,s2):
    if abs(len(s1)-len(s2))>1:
           return False
    i,j,count = 0,0,0
    while i<len(s1) and j<len(s2):
        if s1[i] != s2[j]:
            count+=1
            if i+1 <len(s1) and j+1 <len(s2) and s1[i+1] == s2[j+1]:
                i+=1
                j+=1
            elif i+1 <len(s1) and s1[i+1] == s2[j]:
                i+=1
            elif j+1 < len(s2) and s1[i] == s2[j+1]:
                j+=1
        i+=1
        j+=1
    if i<len(s1) or j<len(s2):
        count+=1
    return count<2

print(oneAway("pale","ples"))
print(oneAway("roval","royal"))
print(oneAway("accd","accd00"))


        
