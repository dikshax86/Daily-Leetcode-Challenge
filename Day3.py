from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        row=len(grid)
        col=len(grid[0])
        dic={}
        
        def dfs(i,j,s):
            
            if i<0 or i>=row or j<0 or j>=col or grid[i][j]!=1:return 
            
            s+=[(i,j)]
            grid[i][j]=2
            
            dfs(i-1,j,s)
            dfs(i,j-1,s)
            dfs(i,j+1,s)
            dfs(i+1,j,s)
            
            return s
        first=second=[]
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    index=dfs(i,j,[])
                    if first==[]:
                        first=index
                    else:
                        second=index
       
        ans=float('inf')
        for i in first:
            for j in second:
                temp=abs(i[0]-j[0])+abs(i[1]-j[1])
                if temp<ans:
                    ans=temp
        return ans-1