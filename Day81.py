class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if not nums or len(nums)==1:return nums
        
        j=0
        i=0
        
        while i<len(nums) and j<len(nums):
            
            if j>=0 and nums[i]%2==0:
                t=nums[j]
                nums[j]=nums[i]
                nums[i]=t
                j+=1   
            
            i+=1
        
        return nums