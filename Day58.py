from heapq import heappush,heappop
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        heap,ans,flag,i,j=[],[],0,0,k-1
        
        for x in range(k):
            heappush(heap, (nums[x]*-1,x))

        while j<len(nums):
            
            while flag==0:
                val=heap[0]
                index=val[1]
                
                if i <= index <= j:
                    ans.append(val[0]*-1)
                    flag=1
                else:
                    heappop(heap)
                    
            i+=1
            j+=1
            
            if j<len(nums):
                heappush(heap,(nums[j]*-1,j))
                flag=0
            
        return ans