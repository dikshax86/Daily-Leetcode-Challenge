class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        def rev(number):
            
            reverse=0
            
            while number>0:
                
                reverse=reverse*10+(number%10)
                number=number//10
                
            return reverse
        
        dic={}
        
        for i in range(len(nums)):
            
            temp=nums[i]-rev(nums[i])
            
            if temp not in dic:
                dic[temp]=1
            else:
                dic[temp]+=1
        
        ans=0
        for i in dic.values():
            
            ans+=(i*(i-1)//2)
            
        return ans%(10**9+7)
