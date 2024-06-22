class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        
        # Traverse the linked list using two pointers
        # Slow pointer moves one step at a time, while fast pointer moves two steps at a time
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # At this point, slow pointer is at the middle node
        return slow