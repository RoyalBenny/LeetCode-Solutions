#Time: O(nlogN)
#Space: O(N)
from heapq import _heapify_max,_heappop_max
def createDict(items):
    idDict = dict()
    for id,score in items:
        if id in idDict:
            idDict[id].append(score)
        else:
            idDict[id] = [score]
    return idDict

def countingSort(ids):
    array = [False]*(max(ids)+1)
    for id in ids:
        array[id] = True
    return array

def calculateHighFive(items):
    idDict = createDict(items)
    ids = countingSort(idDict.keys())
    output =[]
    for i,present in enumerate(ids):
        if not present:
            continue
        scores = idDict[i]
        _heapify_max(scores)
        sum = _heappop_max(scores)+_heappop_max(scores)+_heappop_max(scores)+_heappop_max(scores)+_heappop_max(scores)
        output.append([i,sum//5])
    return output


items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
print(calculateHighFive(items))
        
    
