#Time: O(N)
#Space: O(1)
#String
# https://leetcode.com/problems/string-compression/

def compress(cs):
    p,n,l = 0,0,cs[0]
    for c in cs+['~']:
      if c==l:
        n += 1
      else:
        cs[p],p = l,p+1
        if n>1:
          for nn in str(n):
            cs[p],p = nn,p+1
        n,l = 1,c
    return p,cs[:p]

print(compress(["a","a","b","b","c","c","c"]))
print(compress(["a"]))
print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
