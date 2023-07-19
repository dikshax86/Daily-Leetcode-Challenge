class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals,key=lambda x:x[1])
        prev=-float('inf')
        ans=0
        
        for i in intervals:
            if i[0]>=prev:
                prev=i[1]
            else:
                ans+=1
            
        return ans