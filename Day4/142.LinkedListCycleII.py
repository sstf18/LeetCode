# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # start from head, no need dummy_head since no operations
        slow = head
        fast = head
        # the variable 'fast' and 'fast.next'
        #if no fast.next, the fast.next.next will get wrong
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow: 
                slow = head
                while slow != fast: 
                    slow = slow.next 
                    fast = fast.next 
                return slow
        return None

# Thinking: 
# slow and fast should be head!!! no operation
# fast is one more step ahead 