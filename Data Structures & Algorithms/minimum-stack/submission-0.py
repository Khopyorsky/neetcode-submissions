class MinStack:

    StackItem = namedtuple("StackItem", ["value", "minimum"])

    def __init__(self) -> None:
        self._items: list[MinStack.StackItem] = []

    def push(self, val: int) -> None:
        if not self._items:
            self._items.append(self.StackItem(val, val))
        else:
            self._items.append(
                self.StackItem(val, min(val, self._items[-1].minimum))
            )

    def pop(self) -> None:
        self._items.pop()

    def top(self) -> int:
        return self._items[-1].value


    def getMin(self) -> int | None:
        return self._items[-1].minimum

        
