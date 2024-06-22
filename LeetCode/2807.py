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

# Function to print the linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
if __name__ == "__main__":
    # Create the linked list from the input [18, 6, 10, 3]
    head = ListNode(18)
    head.next = ListNode(6)
    head.next.next = ListNode(10)
    head.next.next.next = ListNode(3)

    # Create a solution object
    solution = Solution()

    # Insert nodes with GCD values
    modified_head = solution.insertGreatestCommonDivisors(head)

    # Print the modified linked list
    print("Original Linked List:")
    printLinkedList(head)

    print("\nModified Linked List:")
    printLinkedList(modified_head)
