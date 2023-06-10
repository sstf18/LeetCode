# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(0, next= head)
        slow = dummy_head
        fast = dummy_head
        for _ in range(1+n):
            fast = fast.next
        # i got wrong on this point, there is no fast.next
        # do not need fast.next, since fast = dummy_head
        while fast: 
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy_head.next

#Thinking: 
# need opeartion so using dummy_head
# fast pointer go n+1 ahead.
# slow.next = slow.next.next is a way to delete node
        