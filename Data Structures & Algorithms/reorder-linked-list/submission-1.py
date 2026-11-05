# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        current = head

        while current and current.next:

            to_move = current
            temp = None

            while to_move.next:
                temp = to_move
                to_move = to_move.next

            if temp:
                temp.next = None

            temp = current.next
            current.next = to_move
            to_move.next = current = temp