from typing import List

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        indegree=[0]*n
        
        self.ans=0
        
        def solve(start,count):
            if start==len(requests):
                for i in indegree:
                    if i!=0:
                        return
                self.ans=max(self.ans,count)
                return 
            
            #take
            indegree[requests[start][0]]-=1
            indegree[requests[start][1]]+=1
            solve(start+1,count+1)
            
            #not 
            indegree[requests[start][0]]+=1
            indegree[requests[start][1]]-=1
            solve(start+1,count)
            
            
        solve(0,0)
        return self.ans