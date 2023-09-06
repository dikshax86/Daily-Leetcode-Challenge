from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        fake=head
        n=0
        while fake:
            n+=1
            fake=fake.next
            
        ans=[]
        
        val=n%k
        keep=head
        limit=n//k
        
        for i in range(k):
            
            if i==val:
                limit=n//k-1
 
            fake=keep
            ans.append(fake)
            for j in range(limit):
                if fake:
                    fake=fake.next
            
            if keep and fake:
                keep=fake.next
                fake.next=None

        return ans

            
            
            
            