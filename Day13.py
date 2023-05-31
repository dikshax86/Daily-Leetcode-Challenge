from typing import Collection

class UndergroundSystem:

    def __init__(self):
        self.entry={}
        self.exit=Collection.defaultdict(list)

    def checkIn(self, id: int, st: str, t: int) -> None:
        self.entry[id]=(st,t)

    def checkOut(self, id: int, st: str, t: int) -> None:
        station,time=self.entry[id]
        self.exit[(station,st)].append((t-time))

    def getAverageTime(self, st1: str, st2: str) -> float:
        
        distance=self.exit.get((st1,st2))
        total=sum(distance)
        length=len(distance)
        return total/length


