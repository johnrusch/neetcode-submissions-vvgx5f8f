# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        l1_num = ""
        while curr:
            l1_num = str(curr.val) + l1_num
            curr = curr.next
        
        l1_num = int(l1_num)

        curr = l2
        l2_num = ""
        while curr:
            l2_num = str(curr.val) + l2_num
            curr = curr.next
        l2_num = int(l2_num)
        res = str(l1_num + l2_num)

        dummy = ListNode(0)
        prev = dummy
        for s in res[::-1]:
            curr = ListNode(int(s))
            prev.next = curr
            prev = curr

        return dummy.next