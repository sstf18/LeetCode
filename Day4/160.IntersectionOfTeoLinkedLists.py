# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 0, 0  
        # length of list A
        cur = headA
        while cur: 
            cur = cur.next
            lenA += 1
        # length of list B
        cur = headB
        while cur: 
            cur = cur.next
            lenB += 1
        curA, curB = headA, headB

        if lenA > lenB: 
            curA, curB = curB, curA
            lenA, lenB = lenB, lenA
          
        for _ in range(lenB - lenA):
            curB = curB.next

        while curA: 
            if curA == curB: 
                return curA
            else: 
                curA = curA.next
                curB = curB.next
        return None

#Thinking: 
# get two length of list 
# let LenB always be the longest, if lenA is longer 
#then lenA need swtich everying with lenB
