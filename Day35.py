from heapq import heappop
import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        l1=len(nums1)
        l2=len(nums2)
        pairs_heap=[]
        ans=[]
        
        for i in range(l1):
            for j in range(l2):
                
                sm=nums1[i]+nums2[j]
                
                val=sm*-1
                
                if len(pairs_heap)<k:
                    heapq.heappush(pairs_heap,(val,[nums1[i],nums2[j]]))
                    
                elif sm<(-1*(pairs_heap[0][0])):
                        heappop(pairs_heap)
                        heapq.heappush(pairs_heap,(val,[nums1[i],nums2[j]]))
                else:
                    break
        
        while k>0:
            if pairs_heap:
                val=heappop(pairs_heap)
                ans.append(val[1])
                k-=1
            else:
                return ans
            
        return ans
            
        
        
        