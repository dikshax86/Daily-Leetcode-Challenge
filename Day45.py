from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        if not pre:return True
        dic=defaultdict(list)
        visited=[-1]*numCourses
        
        for i in pre:
            x,y=i[0],i[1]
            dic[y].append(x)
            
        def dfs_cycle(course):
            if course not in dic:return True
            if visited[course]!=-1:
                return visited[course]==2
            
            visited[course]=1
            for neigh in dic[course]:
                
                if not dfs_cycle(neigh):return False
            
            visited[course]=2
            return True
        
        for i in dic:
            
            if not dfs_cycle(i):
                return False
                
        return True
            
          

            
        
            