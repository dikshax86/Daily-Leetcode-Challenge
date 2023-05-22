from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic={}
        lth=len(nums)
        
        for i in nums:
            if i in dic:
                dic[i]=dic[i]+1
            else:
                dic[i]=1
        
        
        dic1=dict(sorted(dic.items(), key=lambda item:item[1]))
        
        li=list(dic1.keys())
        
        return li[::-1][:k]