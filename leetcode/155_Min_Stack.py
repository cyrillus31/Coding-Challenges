class MinStack:

    def __init__(self):
        self.top_node = None
        self.min = None

    def __repr__(self):
        if self.top_node:
            return str(self.top_node)
        return "None"


    def push(self, val: int) -> None:
        class Node:
            def __init__(self, val=None, prev=None):
                self.val = val
                self.prev = prev

            def __repr__(self):
                if self.prev is None:
                    return f"({self.val} from None)"
                return f"{self.val} from {self.prev}"

        node = Node(val, self.top_node)
        self.top_node = node
        if self.min:
            if val < self.min:
                self.min = val
        else:
            self.min = val

    def pop(self) -> None:
        if self.top_node:
            top_node = self.top_node
            self.top_node = top_node.prev

    def top(self) -> int:
        if self.top_node:
            return self.top_node.val

    def getMin(self) -> int:
        if self.min:
            return self.min

stack = MinStack()
stack.push(-2)
stack.push(22)
stack.pop()
stack.pop()
print(stack.top())

