import collections
from typing import List
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        adj_list=[[] for _ in range(n)]
        
        for (u,v),p in zip(edges,succProb):
            adj_list[u].append([v,p])
            adj_list[v].append([u,p])
        
        pq=[[-1,start]]
        
        distance=collections.defaultdict(int)
        distance[start]=-1
        
        while pq:
            
            d,node=heapq.heappop(pq)
            for nbr,pro in adj_list[node]:
                d2=d*pro
                
                if d2<distance[nbr]:
                    heapq.heappush(pq,[d2,nbr])
                    distance[nbr]=d2
        
        return -distance[end]
        
        