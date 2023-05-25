from heapq import heappop, heappush
from typing import List

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        heap=[]
        total_sum=0
        ans=0
        
        for y,x in sorted(zip(nums2,nums1),reverse=True):
            heappush(heap,x)
            total_sum+=x
            
            if len(heap)>k:
                total_sum-=heappop(heap)
            
            if len(heap)==k:
                ans=max(ans,total_sum*y)
        
        return ans