""" TASK
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit.
 Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself."""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        add = 0
        while l1 or l2 or add:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0

            val = v1 + v2 + add
            add = val//10
            val = val%10
            current.next = ListNode(val)

            current = current.next 
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
        return dummy.next

'''The addTwoNumbers function adds two numbers represented by linked lists,
 where each node contains a single digit (in reverse order).
It uses a dummy head to build the result list and a carry (add) to store overflow.

For each pair of nodes:

It adds their values and the carry.

Creates a new node with the digit part of the sum (val % 10).

Updates the carry (val // 10) for the next iteration.

The loop continues until both lists and the carry are exhausted. This gives an O(n) time solution, where n is the length of the longer list.'''