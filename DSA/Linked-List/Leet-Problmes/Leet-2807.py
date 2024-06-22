# Definition for singly-linked list.
from math import gcd

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head):
        current = head
        while current and current.next:
            gcd_value = gcd(current.val, current.next.val)
            new_node = ListNode(gcd_value)

            new_node.next = current.next
            current.next = new_node

            current = current.next.next

        return head