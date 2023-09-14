import collections
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj=collections.defaultdict(list)
        ans=[]
        
        for i,j in sorted(tickets, reverse=True):
            adj[i].append(j)
        
        def dfs(key):
            while adj[key]:
                dfs(adj[key].pop())
            ans.append(key)
        
        dfs("JFK")
        return ans[::-1]