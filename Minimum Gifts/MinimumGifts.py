#T: O(N*cubics^cubics) S: O(N)
def findGifts(arr,index):
    count = 0
    left = index-1
    while left>=0 and arr[left]:
        count+=1
        left-=1
    right = index+1
    while right<len(arr) and arr[right]:
        count+=1
        right+=1
    return count

minGift = float('Inf')
output = []
def findMin(cubics,gifts,arr,order):
    global minGift
    global output
    if not cubics:
        if gifts<minGift:
            output = order
        minGift = min(minGift,gifts)
        return 
    if gifts > minGift:
        return 
    for i in range(len(cubics)):
        arr[cubics[i]] = False
        findMin(cubics[:i]+cubics[i+1:],gifts+findGifts(arr,cubics[i]),arr,order+[cubics[i]])
        arr[cubics[i]] = True

numOfEmployees = 10000
cubics = [50,18,24,999,114,0,998]
arr = [True]*(numOfEmployees)
findMin(cubics,0,arr,[])
print(minGift,output)
        
