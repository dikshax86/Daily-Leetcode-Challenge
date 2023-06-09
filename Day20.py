from typing import List
class Solution:
        
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        row,col=len(grid),len(grid[0])
        j=0
        for i in range(row-1,-1,-1):
            if j==col:
                break
            while j<col:
                if grid[i][j]<0:
                    count+=(col-j)
                    break
                j+=1  
        return count
        
        