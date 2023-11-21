class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        counter=0
        nums=sorted(nums)
        ans=0
        
        for i in range(1,len(nums)):
    
            if nums[i]>nums[i-1]:
                ans+=(counter+1)
                counter+=1
            else:
                ans+=counter
        
        return ans
