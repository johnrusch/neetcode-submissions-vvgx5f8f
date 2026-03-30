# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        curr1, curr2 = head, prev

        while curr1 and curr2:
            next1, next2 = curr1.next, curr2.next
            curr1.next = curr2

            if next1:
                curr2.next = next1
            else:
                break

            curr1 = next1
            curr2 = next2