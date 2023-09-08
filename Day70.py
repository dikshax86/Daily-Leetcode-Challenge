from typing import List

class Solution:
    def generate(self, n: int) -> List[List[int]]:
        
        ans=[[1]]
        
        for i in range(1,n):
            
            li=[1]
            first=0
            second=1
            
            for j in range(1,i):
                
                li.append(ans[-1][first]+ans[-1][second])
                first+=1
                second+=1
                
            li.append(1)
            ans.append(li)
            
        return ans
                