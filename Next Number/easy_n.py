def getNext(n):
    c,c0,c1 = n,0,0
    while (c&1)==0 and c!=0:
        c0+=1
        c >>= 1

    while (c&1) == 1:
        c1+=1
        c >>= 1
    if c0+c1 == 31 or c0+c1 == 0:
        return -1
    return n+(1<<c0)+ (1<<(c1-1))-1


def getPrev(n):
    c,c0,c1 = n,0,0
    while (c&1)==1:
        c1+=1
        c >>= 1
    if not c:
        return -1

    while (c&1)==0 and c:
        c0+=1
        c>>=1

    return n- (1<<c1) - (1 << (c0-1))+1

n = int(input("Enter number"))
print("Smallest " ,getPrev(n))
print("Largest " , getNext(n))
