# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def getDecimalValue(self, head) -> int:
        answer = ""

        current = head
        while current:
            answer += str(current.val)
            current = current.next

        return int(answer,2)