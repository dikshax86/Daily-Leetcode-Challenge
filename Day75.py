from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans=[]
        
        for i in range(len(mat)):
            tup=0
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    tup+=1
            ans.append((i,tup))
                    
        ans=sorted(ans,key=lambda x:x[1])
        
        li=[]
        for i in range(k):
            li.append(ans[i][0])
            
        return li