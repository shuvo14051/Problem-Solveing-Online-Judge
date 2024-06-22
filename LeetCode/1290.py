class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        answer = ""
        current = head
        while current:
            answer += str(current.val)
            current = current.next

        return int(answer,2)
    

def list_to_linkedlist(items):
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head
    
s = Solution()
print(s.getDecimalValue(list_to_linkedlist([1,0,1])))

        