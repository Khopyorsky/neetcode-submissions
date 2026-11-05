# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = fast = head

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        second_half_head = slow.next  
        slow.next = None  


        prev = None
        while second_half_head:
            next_one = second_half_head.next
            second_half_head.next = prev
            prev = second_half_head
            second_half_head = next_one

        first = head
        second = prev

        while second:
            next_in_first = first.next 
            next_in_second = second.next

            first.next = second
            second.next = next_in_first

            first = next_in_first
            second = next_in_second