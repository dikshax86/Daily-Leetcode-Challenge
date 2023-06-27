from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        dp=[[-1]*10010 for _ in rods]
        
        def tb(i,diff):
            
            if i==len(rods):
                if not diff: return 0
                return -1e9
            
            if dp[i][diff+5000]!=-1:return dp[i][diff+5000]
            
            op1=rods[i]+tb(i+1,diff+rods[i])
            op2=tb(i+1,diff-rods[i])
            op3=tb(i+1,diff)
            
            dp[i][diff+5000]=max(max(op1,op2),op3)
            
            return dp[i][diff+5000]
        
        return tb(0,0)
            
        