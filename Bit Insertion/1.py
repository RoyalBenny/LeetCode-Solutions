def bitInsertion(N,M,i,j):
    mLen = len(bin(M))-2 if M >=0 else len(bin(M))-3
    print(mLen)
    mask = (-1 << j+1 ) | ((1 << i)-1)
    masked = N & mask
    M = M << i
    return masked | M

result = (bitInsertion(1201,8,3,6))
print(result,bin(result))
    
