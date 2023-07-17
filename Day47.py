# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def addLength(length):
            zeros=ListNode()
            fake=zeros
            while length:
                fake.next=ListNode(0)
                length-=1
                fake=fake.next
            return zeros.next
            
        def reverse(head):
            prev=None
            cur=head
            front=None
            
            
            while cur:
                front=cur.next
                cur.next=prev
                prev=cur
                cur=front
            
            return prev
            
        n1=l1
        n2=l2
        
        lth1,lth2=0,0
        while l1.next:
            lth1+=1
            l1=l1.next
        while l2.next:
            lth2+=1
            l2=l2.next
        
        if lth1<lth2:
            zeros=addLength(lth2-lth1)
            zero=zeros
            while zero.next:
                zero=zero.next                
            zero.next=n1
            n1=zeros
        
        elif lth1>lth2:
            zeros=addLength(lth1-lth2)
            zero=zeros
            while zero.next:
                zero=zero.next                
            zero.next=n2
            n2=zeros
          
        
        first=reverse(n1)
        second=reverse(n2)
        
        ans=ListNode()
        fake=ans
        
        carry=0
        while first:
            value=carry+first.val+second.val
            fake.next=ListNode(value%10)
            
            carry=value//10
            first=first.next
            second=second.next
            fake=fake.next
        
        if carry:
            fake.next=ListNode(carry)
       
        return reverse(ans.next)