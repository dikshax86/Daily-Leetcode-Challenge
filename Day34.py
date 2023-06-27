from heapq import heappop, heappush
from math import inf
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        i=0
        j=len(costs)-1
        cost=0
        left_minh=[]
        right_minh=[]
        
        while k>0:
            
            while len(left_minh)<candidates and i<=j:
                heappush(left_minh,costs[i])
                i+=1
                
            while len(right_minh)<candidates and i<=j:
                heappush(right_minh,costs[j])
                j-=1
                
            t1=left_minh[0] if left_minh else float(inf)
            t2=right_minh[0] if right_minh else float(inf)
            
            if t1<=t2:
                cost+=t1
                heappop(left_minh)
            else:
                cost+=t2
                heappop(right_minh)
            
            k-=1
        
        return cost
        