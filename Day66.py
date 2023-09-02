from typing import List
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        dp=[0]*51
        n=len(s)
        
        for i in range(n-1,-1,-1):
            
            dp[i]=dp[i+1]+1
            
            for w in dictionary:
                if (i+len(w))<=n and s[i:i+len(w)]==w:
                    dp[i]=min(dp[i],dp[i+len(w)])
                    
        return dp[0]