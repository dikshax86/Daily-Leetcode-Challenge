class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        max_heap=[]
        
        for i in nums:
            heappush(max_heap,i*-1)
            
        while k>1:
            heappop(max_heap)
            k-=1
        
        return (heappop(max_heap)*-1)