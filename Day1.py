class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color=[-1]*n
        
        for i in range(n):
            if color[i]==-1:
                queue=[i]
                color[i]=0
                
                while queue:
                    
                    node=queue.pop()
                    
                    for neighbour in graph[node]:
                        
                        if color[neighbour]==-1:
                            queue.append(neighbour)
                            color[neighbour]=1-color[node]
                        else:
                            if color[neighbour]==color[node]:
                                return False
        return True