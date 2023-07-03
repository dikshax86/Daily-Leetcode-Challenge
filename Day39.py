from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        l1=Counter(s)
        l2=Counter(goal)
        
        if l1==l2:
            if s==goal:
                for i in l1:
                    if l1[i]>1:return True
                return         
                
            ct=0
            for i in range(len(s)):
                
                if s[i]!=goal[i] and ct>=2:
                    return False
                    
                if s[i]!=goal[i] and ct<2:
                    ct+=1
                
            return True
                