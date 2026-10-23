# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous: ListNode | None = None
        while head:
            next_one = head.next
            head.next = previous
            previous = head
            head = next_one

        return previous