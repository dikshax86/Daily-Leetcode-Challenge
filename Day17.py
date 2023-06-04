from collections import defaultdict
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        dic=defaultdict(list)
        lth=len(isConnected)
        visited=set()
            
        for i in range(lth):
            for j in range(lth):
                if i!=j and isConnected[i][j]==1:
                    dic[i].append(j)
        
        
        def dfs(root):
            for x in dic[root]:
                if x not in visited:
                    visited.add(x)
                    dfs(x)
        
        ct=0
        for val in range(lth):
            if val not in visited:  
                dfs(val)
                ct+=1

        return ct
        
            
        
        