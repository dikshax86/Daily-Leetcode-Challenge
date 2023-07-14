class Solution:
    def longestSubsequence(self, arr: List[int], k: int) -> int:
        dp=defaultdict(int)
        mx=0
        
        for i in arr:
            dp[i]=dp[i-k]+1
            mx=max(dp[i],mx)
            
        return mx