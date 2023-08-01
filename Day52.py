class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        self.ans=[]
        
        def generate_comb(start,current):
            
            if len(current)==k:
                
                self.ans.append(current.copy())
                
                return 
            
            for i in range(start,n+1):
                current.append(i)
                generate_comb(i+1,current)
                current.pop()
        
        generate_comb(1,[])
        
        return self.ans
        
       