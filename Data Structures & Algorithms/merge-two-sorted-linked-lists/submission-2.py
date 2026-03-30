# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        dummy = ListNode()
        prev = dummy

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                prev.next = curr1
                temp = curr1.next
                prev = curr1
                curr1 = temp
            else:
                prev.next = curr2
                temp = curr2.next
                prev = curr2
                curr2 = temp

        if curr1 and not curr2:
            prev.next = curr1
        elif curr2 and not curr1:
            prev.next = curr2
        
        return dummy.next
