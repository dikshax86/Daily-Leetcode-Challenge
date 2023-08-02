from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans=[]
        
        def generate_perm(start,cur):
            
            if len(cur)==len(nums):
                ans.append(cur.copy())
            
            for i in range(0,len(nums)):
                
                if nums[i] in cur:continue
                
                cur.append(nums[i])
                generate_perm(i+1,cur)
                cur.pop()
                
        
        generate_perm(0,[])
        
        return ans