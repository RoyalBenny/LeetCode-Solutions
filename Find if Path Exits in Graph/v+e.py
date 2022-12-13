# Time : O(v+e)
# Space: O(e)
# https://leetcode.com/problems/find-if-path-exists-in-graph/
from queue import Queue
class Graph:
    def __init__(self,n):
        self.n = n
        self.list = [None]*n

class Node:
    def __init__(self,val):
        self.val = val
        self.list = []

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n <= 1 :
            return True
        G = self.createAdjList(n,edges)
        return self.BFS(G,source,destination)
    
    def createAdjList(self,n,edges):
        G = Graph(n)
        for s,e in edges:
            self.addNode(s,e,G)
            self.addNode(e,s,G)
        return G
    
    def addNode(self,s,e,G):
        if not G.list[s]:
            G.list[s] = Node(s)
        G.list[s].list.append(e)
    
    def BFS(self,G,S,D):
        visited = [False]*G.n
        queue = Queue(maxsize = 0)
        queue.put(S)
        while not queue.empty():
            node = queue.get()
            visited[node] = True
            for i in G.list[node].list:
                if i == D:
                    return True
                if not visited[i]:
                    queue.put(i)
        return False
        
