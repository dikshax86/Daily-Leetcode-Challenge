from typing import List

class Solution:
    def letterCombinations(self, digi: str) -> List[str]:
        if not digi:return 
        dic={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        ans=[]
        
        def generate_pattern(start,st):
            
            if len(st)==len(digi):
                ans.append(st)
            
            for i in range(start,len(digi)):
                
                for j in range(len(dic[digi[i]])):
                
                    st+=(dic[digi[i]][j])

                    generate_pattern(i+1,st)

                    st=st[:-1]
                
        generate_pattern(0,"") 
        
        return ans                                                                                