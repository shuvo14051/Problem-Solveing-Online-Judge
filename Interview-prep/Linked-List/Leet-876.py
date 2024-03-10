class ListNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Solution:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def append_at_end(self, data):
        node = ListNode(data)
        
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

        self.size += 1

    def middleNode(self):
        slow = self.head
        fast = self.head
        
        # Traverse the linked list using two pointers
        # Slow pointer moves one step at a time, while fast pointer moves two steps at a time
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # At this point, slow pointer is at the middle node
        # Traverse from the middle node to the end and store the values in a list
        result = []
        while slow:
            result.append(slow.data)
            slow = slow.next
        
        return result

s = Solution()
s.append_at_end(1)
s.append_at_end(2)
s.append_at_end(3)
s.append_at_end(4)
s.append_at_end(5)

values_from_middle_to_end = s.middleNode()
print(values_from_middle_to_end)  # Output should be [3, 4, 5]
