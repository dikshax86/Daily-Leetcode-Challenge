from typing import List
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        i=0
        inc,dec=0,0

        while i<len(nums)-1:
            if nums[i]<nums[i+1]:
                inc=1
            elif nums[i]>nums[i+1]:
                dec=1
            if inc and dec:return False
            i+=1
        
        return True
    
        