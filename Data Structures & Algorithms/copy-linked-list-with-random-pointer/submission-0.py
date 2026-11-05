"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        copies: dict[Node, Node] = {}

        current = head
        while current:
            copies[current] = Node(current.val)
            current = current.next

        for original, copy in copies.items():
            assert original
            copy.next = copies.get(original.next)
            copy.random = copies.get(original.random)

        return copies[head]