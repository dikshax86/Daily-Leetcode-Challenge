from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:return len(nums)-1
        count=0
        arr=[]
        
        for i in nums:
            
            if i==0:
                arr.append(count)
                count=0
            
            if i==1:
                count+=1
                
        arr.append(count)
        
        ans=0
        for i in range(1,len(arr)):
            sm=arr[i]+arr[i-1]
            ans=max(ans,sm)
        
        return ans