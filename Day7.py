class Solution:
    def new21Game(self, n: int, k: int, w: int) -> float:
        if k==0 or n>=(k+w):return 1
        
        dp=[1.0]+[0.0]*n
        
        #store total value sum
        total,res=1.0,0.0
        
        for i in range(1,n+1):
            dp[i]+=total/w
            if i<k:
                total+=dp[i]
            else:
                res+=dp[i]
            if i-w>=0:
                total-=dp[i-w]
        
        return res