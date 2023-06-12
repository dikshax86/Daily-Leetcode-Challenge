from math import inf
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        nums.append(float(inf))
        ans=[]
        lth=len(nums)
        st=""
        
        
        for i in range(lth-1):
            if nums[i]==(nums[i+1]-1):
                if not st:
                    st=str(nums[i])

            else:
                if st:
                    ans.append(st+"->"+str(nums[i]))
                else:
                    ans.append(str(nums[i]))
                st=""
        
        return ans