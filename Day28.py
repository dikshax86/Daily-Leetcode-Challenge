class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        ans=prev=n=0
        
        for i in gain:
            n=i+prev
            prev=n
            ans=max(ans,n)
            
        return ans
        
        