class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        prefix_sum=[0]*len(nums)
        prefix_sum[0]=nums[0]
        avg=(2*k+1)
        ans=[-1]*len(nums)
        
        for i in range(1,len(nums)):
            prefix_sum[i]=prefix_sum[i-1]+nums[i]
            
        for i in range(k,len(nums)-k):
            if (i-k-1)<0:
                ans[i]=(prefix_sum[i+k]//avg)
            else:
                ans[i]=(prefix_sum[i+k]-prefix_sum[i-k-1])//avg
            
        return ans
        
        