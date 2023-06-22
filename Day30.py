class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        tuple_arr=[(a,b) for a,b in zip(nums,cost)]
        tuple_arr=sorted(tuple_arr)
        
        res=0
        
        prec=[tuple_arr[0][1]]+[0]*(len(nums)-1)
        posc=[0]*(len(nums)-1)+[tuple_arr[-1][1]]
        
        nc=[a*b for a,b in tuple_arr]
        
        
        prenc=[nc[0]]+[0]*(len(nums)-1)
        posnc=[0]*(len(nums)-1)+[nc[-1]]
        
        for i in range(1,len(nums)):
            prenc[i]=prenc[i-1]+nc[i]
            prec[i]=prec[i-1]+tuple_arr[i][1]
            
        for i in range(len(nums)-2,-1,-1):
            posnc[i]=nc[i]+posnc[i+1]
            posc[i]=tuple_arr[i][1]+posc[i+1]
        
        
        ans = float('inf')
        for i in range(len(nums)):
            
            res = 0
            
            if i==0:
                res=posnc[i+1]-tuple_arr[i][0]*posc[i+1]
                
            
            elif (i==len(nums)-1):
                res=tuple_arr[i][0]*prec[i-1]-prenc[i-1]
                
                
            else:
                res=posnc[i+1]-tuple_arr[i][0]*posc[i+1]
                res+=tuple_arr[i][0]*prec[i-1]-prenc[i-1]
                
            ans = min(ans,res)
            
        return ans
        