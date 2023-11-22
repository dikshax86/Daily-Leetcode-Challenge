class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        dic=collections.defaultdict(list)
        
        for i in range(len(nums)):
            
            for j in range(len(nums[i])):
                
                dic[i+j].insert(0,nums[i][j])
                
        ans=[]
        
        for i in dic.values():
            
            for j in i:
                ans.append(j)
        
        return ans
