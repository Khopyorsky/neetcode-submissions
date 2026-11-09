class Node:  # noqa

    def __init__(
        self,
        key: int | None = None,
        val: int | None = None,
        prv: Node | None = None,
        nxt: Node | None = None,
    ) -> None:

        self.key: int | None = key
        self.val = val
        self.prev = prv
        self.next = nxt


# НОВЫЕ В НАЧАЛО СПИСКА


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.cache: dict[int, Node] = {}
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        assert node.val is not None and node.key is not None

        left = node.prev
        right = node.next

        assert left and right

        left.next = right
        right.prev = left

    def _add_to_front(self, node: Node) -> None:

        front = self.head.next
        assert front

        if front is node:
            return

        self.head.next = node
        node.prev = self.head
        node.next = front
        front.prev = node

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_front(node)
            return
        if len(self.cache) == self.capacity:
            to_delete = self.tail.prev

            assert to_delete is not None and to_delete.key is not None

            self._remove(to_delete)
            del self.cache[to_delete.key]

        node = Node(key, value)
        self._add_to_front(node)
        self.cache[key] = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)

        return node.val  # type: ignore