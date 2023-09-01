from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        
        dp=[-1]*(n+1)
        res=[0]*(n+1)
        
        def get_binary(num):
            
            if num==0:return 0
            if num==1:return 1
            
            if dp[num]!=-1:return dp[num]
            
            if num%2!=0:
                dp[num]=1+get_binary(num//2)
            else:
                dp[num]=get_binary(num//2)
            
            return dp[num]
        
        for i in range(n+1):
            
            res[i]=get_binary(i)
            
        return res