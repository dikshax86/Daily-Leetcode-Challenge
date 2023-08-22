class Solution:
    def convertToTitle(self, n: int) -> str:
        
        s=''
        
        while n>0:
            
            r=n%26
            
            if r==0:r=26
                
            s=chr(r+64)+s
            
            n=int((n-r)/26)
        
        return s