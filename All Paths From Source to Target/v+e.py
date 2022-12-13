#Time: O(v+e)
# Space: O(v+e)
# https://leetcode.com/problems/all-paths-from-source-to-target/
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        output  =[]
        self.DFS(output,graph,0,[0],len(graph)-1)
        return output
    def DFS(self,output,graph,index,visited,end):
        for i in graph[index]:
            visited.append(i)
            if i == end:
                output.append(visited.copy())
            else:
                self.DFS(output,graph,i,visited,end)
            visited.pop(-1)
        
