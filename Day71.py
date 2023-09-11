import collections
from typing import List


class Solution:
    def groupThePeople(self, group: List[int]) -> List[List[int]]:
        dic=collections.defaultdict(list)
        ans=[]
        
        for i,j in enumerate(group):

            if j in dic and len(dic[j])==j:
                ans.append(dic[j])
                dic[j]=[]
            dic[j].append(i)
        
        for i in dic:
            ans.append(dic[i])
            
        return ans