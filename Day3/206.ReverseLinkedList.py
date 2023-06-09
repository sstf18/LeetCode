# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head 
        pre = None
        while curr: 
            temp = curr.next
            curr.next = pre 
            pre = curr
            curr = temp 
        return pre

#Thinking: 
# 1. this way used two pointers in a singly-linked list. 
# 2. difference between 'pre' and 'dummy_head' is that 'pre' is pointer, but 'dummy_head' is a node
# 3. temp stores the value of curr.next before curr