class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        ans=0
        dp=[[-1]*1010 for i in range(len(nums))]
        
        for i in range(1,len(nums)):
            for j in range(0,i):
                
                d=nums[i]-nums[j]
                if dp[j][d+500]!=-1:
                    dp[i][d+500]=1+dp[j][d+500]
                else:
                    dp[i][d+500]=2
                    
                ans=max(ans,dp[i][d+500])
                
        return ans