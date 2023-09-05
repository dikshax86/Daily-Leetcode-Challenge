from typing import Collection, Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        dic=Collection.defaultdict(lambda: Node(0))
        dic[None]=None
        n=head
        fake=n
        
        while n:
            
            dic[n].val=n.val
            dic[n].next=dic[n.next]
            dic[n].random=dic[n.random]
            n=n.next
            
        return dic[fake]