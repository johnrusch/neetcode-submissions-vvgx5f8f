# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # use slow fast pointers to find middle
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None

        # use slow (curr) pointer to reverse back half
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # combine og front with reversed back half
        curr1, curr2 = head, prev
        while curr1 and curr2:
            next1, next2 = curr1.next, curr2.next
            curr1.next = curr2

            if next1:
                curr2.next = next1

            curr1, curr2 = next1, next2
            