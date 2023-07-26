from math import ceil
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        ans=-1
        
        l=1
        r=10**7
        
        while l<=r:
            
            time=0
            
            avg=(l+r)//2
            
            for i in range(len(dist)-1):
                time+=ceil(dist[i]/avg)
                
            time+=dist[-1]/avg
            
            if time>hour:
                l=avg+1
            else:
                ans=avg
                r=avg-1
                
        return ans
                