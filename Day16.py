from typing import Collection, List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        dic=Collection.defaultdict(list)
        
        for i in range(len(manager)):
            dic[manager[i]].append(i)
            
        def dfs(root):
            if root not in dic:return 0
            val=0
            for x in dic[root]:
                
                val=max(val,dfs(x))
                
            return val+informTime[root]
        
        
        return dfs(headID)