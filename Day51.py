class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        lth=max(len(s1),len(s2))+1
        
        dp=[[-1]*(lth) for _ in range(lth)]
        
        def lcs(l1,l2):
            if l1<0 or l2<0:return 0
            
            if dp[l1][l2]!=-1:return dp[l1][l2]
            
            if s1[l1]==s2[l2]:
                dp[l1][l2]=ord(s1[l1])+ord(s2[l2])+lcs(l1-1,l2-1)
                return dp[l1][l2]
                
            dp[l1][l2]=max(lcs(l1-1,l2),lcs(l1,l2-1))
            
            return dp[l1][l2]
        
        value=lcs(len(s1)-1,len(s2)-1)
        tsum=0
        for c in s1:
            tsum+=ord(c)
        for c in s2:
            tsum+=ord(c)
        
        print(value)
        return tsum-value
                     
        