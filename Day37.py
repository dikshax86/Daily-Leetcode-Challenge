import collections
from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        row=len(grid)
        col=len(grid[0])
        keys=0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='@':
                    start=[i,j]
                elif grid[i][j] in 'abcdef':
                    keys+=1
        
        queue=collections.deque([(start[0],start[1],'')])
        seen=set()
        directions=[(0,1),(0,-1),(-1,0),(1,0)]
        moves=0
        
        while queue:
            for _ in range(len(queue)):
                r,c,key=queue.popleft()
                if (r,c,key) in seen:
                    continue
                if len(key)==keys:
                    return moves

                seen.add((r,c,key))

                for rx,ry in directions:
                    nx=rx+r
                    ny=ry+c

                    if nx>=0 and nx<row and ny>=0 and ny<col and grid[nx][ny]!='#':
                        cl=grid[nx][ny]
                        if cl in 'ABCDEF' and cl.lower() in key:
                            queue.append((nx,ny,key))
                        elif cl in '.@':
                            queue.append((nx,ny,key))
                        elif cl in 'abcdef':
                            if cl not in key:
                                queue.append((nx,ny,key+cl))
                            else:
                                queue.append((nx,ny,key))

            moves+=1

        return -1