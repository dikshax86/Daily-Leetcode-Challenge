from heapq import heappush,heappop
class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s or len(s)==1:return s
        
        heap,letters=[],[0]*26
        
        for i in s:
            letters[ord(i)-97]+=1
        
        for i,count in enumerate(letters):
            if count:
                heappush(heap,(-count,chr(i+97)))
            
        if len(heap)==1:return ""    
        
        ans=""
        
        for i in range(len(s)):
            pair=heappop(heap)
            
            if ans and pair[1]==ans[-1]:
                
                pair2=heappop(heap)
                ans+=pair2[1]
                heappush(heap,((pair2[0]+1),pair2[1]))
                heappush(heap,pair)

            else:
                ans+=pair[1]
                heappush(heap,((pair[0]+1),pair[1]))
        
        
        l2=[0]*26
        for i in range(len(ans)):
            l2[ord(ans[i])-97]+=1
        
        return ans if letters==l2 else ""