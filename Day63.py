from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs=sorted(pairs,key=lambda x:x[1])
        
        i,j=0,1
        ans=1
        
        while j<len(pairs):
            if pairs[i][1]<pairs[j][0]:
                ans+=1
                i=j
            j+=1
            
        
        return ans