from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        def bs_alpha():

            l=0
            r=len(letters)-1
            flag=-1
            
            while l<=r:
                mid=(l+r)//2

                if letters[mid]<=target:
                    l=mid+1
                else:
                    flag=mid
                    r=mid-1
            return flag
        
        val=bs_alpha()
        
        return letters[val] if val!=-1 else letters[0]
            
    
                