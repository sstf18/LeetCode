# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next = head
        current = dummy_head
        while current.next: 
            if current.next.val == val: 
                current.next = current.next.next
            else: 
                current = current.next 
        return dummy_head.next

#THinking: 
# create dummy_head, if we want to opearte one node, we have to find the previous node. 
        