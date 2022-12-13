# Time : O(V+E)
# Space: O(V+E)
# Graph
# https://leetcode.com/problems/course-schedule-ii/
class Solution:
    def findOrder(self, num: int, pre: List[List[int]]) -> List[int]:
        if not pre:
            return list(range(num))
        visited = [False]*num
        output = []
        cycle = False
        completed = set()
        adjList = self.createDict(pre,num)
        for i in adjList:
            if not adjList[i]:
                output.append(i)
                completed.add(i)
        if not output:
            return []
        for i in adjList:
            if i not in completed:
                visited[i] = True
                cycle = self.schedule(adjList,visited,completed,output,i)
                if cycle:
                    return []
                visited[i] = False
        return output
    
    def createDict(self,pre,num):
        D = dict()
        for i,j in pre:
            if i not in D:
                D[i] = [j]
            else:
                D[i].append(j)
        for i in range(num):
            if i not in D:
                D[i] =[]
        return D
    
    def schedule(self,adj,v,c,out,key):
        cycle = False
        if not adj[key]:
            out.append(key)
            c.add(key)
            return False
        for i in adj[key]:
            if i in c:
                continue
            if v[i]:
                return True
            v[i] = True
            cycle = self.schedule(adj,v,c,out,i)
            if cycle:
                return True
            v[i] = False
        out.append(key)
        c.add(key)
        return False
        
