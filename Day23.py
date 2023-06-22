class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hashtable={}
        count=0

        for j in range(len(grid[0])):
            column=tuple([row[j] for row in grid])
            if column in hashtable:
                hashtable[column]+=1
            else:
                hashtable[column]=1
        
        
        
        for i in grid:
            row=tuple(i)
            if row in hashtable:
                count+=hashtable[row]
        
        return count