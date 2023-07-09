class Solution:
    def putMarbles(self, w: List[int], k: int) -> int:
        
        sum_arr=[]
        ans=0
        
        for i in range(len(w)-1):
            sum_arr.append(w[i]+w[i+1])
            
        sum_arr.sort()
        
        
        for i in range(k-1):
            ans+=sum_arr[len(sum_arr)-1-i]-sum_arr[i]
            
        
        return ans
            