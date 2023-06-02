from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        if grid[0][0]==1 or grid[row-1][col-1]==1:return -1
        
        
        def bfs(i,j):
            
            ax=[-1,0,1,0,1,-1,1,-1]
            ay=[0,-1,0,1,1,-1,-1,1]
            
            queue=[(0,0)]
            grid[0][0]=1
            
            while queue:
                
                i,j=queue.pop(0)
            
                for k in range(8):
                    nx=i+ax[k]
                    ny=j+ay[k]

                    if nx>=0 and nx<row and ny>=0 and ny<col and grid[nx][ny]==0 :
                        queue.append((nx,ny))
                        grid[nx][ny]=grid[i][j]+1
                    
            
        bfs(0,0)
        return grid[row-1][col-1] if grid[row-1][col-1]>0 else -1