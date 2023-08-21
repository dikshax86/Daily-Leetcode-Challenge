import collections
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        graph=collections.defaultdict(set)
        ans=0
        
        for i,j in roads:
            graph[i].add(j)
            graph[j].add(i)
        
        for c1 in range(n):
            for c2 in range(c1+1,n):
                
                connection=1 if c1 in graph[c2] else 0
                
                ans=max(ans,(len(graph[c1])+len(graph[c2])-connection))
        
        return ans