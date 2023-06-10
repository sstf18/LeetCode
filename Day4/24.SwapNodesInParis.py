# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0, next=head)
        curr = dummy_head
        while curr.next and curr.next.next: 
            temp1 = curr.next
            temp2 = curr.next.next.next
            curr.next = curr.next.next
            curr.next.next = temp1
            temp1.next = temp2
            curr = curr.next.next
        return dummy_head.next

# using temp to store node 