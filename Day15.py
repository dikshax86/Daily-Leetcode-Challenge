from collections import defaultdict
from typing import List
#main
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n,max_detonated_bombs,graph=len(bombs),0,defaultdict(list)
        
        for i in range(n):
            for j in range(n):
                if i==j:continue
                    
                x1,x2,y1,y2=bombs[i][0],bombs[j][0],bombs[i][1],bombs[j][1]
                
                if (bombs[i][2]**2)>=((x1-x2)**2+(y1-y2)**2):
                    graph[i]+=[j]
                    
                    
        def dfs(node,visited):
            for x in graph[node]:
                if x not in visited:
                    visited.add(x)
                    dfs(x,visited)
            
            
        for i in range(n):
            visited=set([i])
            dfs(i,visited)
            max_detonated_bombs=max(max_detonated_bombs,len(visited))
        
        return max_detonated_bombs
    