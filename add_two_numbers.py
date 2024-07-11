#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def Add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        tale = head
        total = carry = 0

        while l1 or l2 or carry != 0:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            num = total % 10
            carry = total // 10
            head.next = ListNode(num)
            head = head.next

        return tale.next

# Helper function to create a linked list from a list of integers
def create_linked_list(nums):
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

# Example usage:
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])

solution = Solution()
result = solution.Add_two_numbers(l1, l2)

print("Resultant linked list:")
print_linked_list(result)