from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr=sorted(nums)
        self.k1=k-1
 
    
    def add(self, val: int) -> int:
        
        self.arr.append(val)
        self.arr=sorted(self.arr)[::-1]
        
        return self.arr[self.k1]