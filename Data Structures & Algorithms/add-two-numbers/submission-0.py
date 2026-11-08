# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = head = ListNode()
        carry = 0
        while l1 or l2:
            res_value = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            node_value = res_value % 10
            carry = res_value // 10
            head.next = ListNode(node_value)
            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            head.next = ListNode(carry)

        return start.next
        