<<<<<<< HEAD
from typing import List
=======

from typing import List

>>>>>>> ab60aa621108bdbc448b720ed2eb1bf893a6d9a5
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph={}
        res=[]
        
        def buildgraph():
            for i in range(len(equations)):
                divident,divisor=equations[i]
                quotient=values[i]
                
                if divident not in graph:
                    graph[divident]=[(divisor,quotient)]
                else:
                    graph[divident].append((divisor,quotient))
                
                if divisor not in graph:
                    graph[divisor]=[(divident,(1/quotient))]
                else:
                    graph[divisor].append((divident,(1/quotient)))
        
        def dfs(start,end):
            
            if start not in graph or end not in graph:return -1.0
            
            if start==end:return 1.0
            visited.add(start)
            for value,weight in graph[start]:
                if value not in visited:
                    result=dfs(value,end)
                    if result!=-1:
                        return (result*weight)
            
            return -1.0
            
        buildgraph()
        for i in queries:
            visited=set()
            res.append(dfs(i[0],i[1]))
        
        return res