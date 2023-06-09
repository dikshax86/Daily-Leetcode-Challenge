from typing import List
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)==2:return True
        
        x1,y1=coordinates[0]
        x2,y2=coordinates[1]

        for x3,y3 in coordinates[2:]:
            if (x3-x2)*(y2-y1)!=(y3-y2)*(x2-x1):
                return False

        return True