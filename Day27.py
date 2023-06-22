class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        row=len(grid)
        col=len(grid[0])
        mod=10**9+7
        
        dp=[[-1]*len(grid[0]) for _ in range(len(grid))]
        
        def dfs(i,j,prev):
            
            if i<0 or j<0 or i>=row or j>=col or prev>=grid[i][j]:
                return 0
            
            if dp[i][j]!=-1:return dp[i][j]
            
            count=1
            
            count+=dfs(i,j+1,grid[i][j])%mod
            count+=dfs(i,j-1,grid[i][j])%mod
            count+=dfs(i+1,j,grid[i][j])%mod
            count+=dfs(i-1,j,grid[i][j])%mod
            
            dp[i][j]=count
            
            return dp[i][j]
        
        count=0
        
        for i in range(row):
            for j in range(col):
                count+=dfs(i,j,-1)
                
        return count%mod
        