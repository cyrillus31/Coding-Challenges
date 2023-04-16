class Queue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    @classmethod
    def create_node(csl, value=None, next=None):
        class Node:
            def __init__(self, value=None, next=None):
                self.value = value
                self.next = next
        return Node(value, next)

    def enqueue(self, value):
        self.length += 1
        enqueued_node = Queue.create_node(value)
        if not self.tail:
            self.head = self.tail = enqueued_node 
            return
        
        enqueued_node = Queue.create_node(value)
        self.tail.next = enqueued_node
        self.tail = enqueued_node

    def deque(self):
        if not self.head:
            return
        self.length -= 1
        dequed_value = self.head.value
        self.head = self.head.next
        return dequed_value

    def peek(self):
        if self.head:
            return self.head.value

if __name__ == '__main__':
    q = Queue()

    q.enqueue('first')
    q.enqueue('second')

    print(q.tail is q.head)
    print(q.head.next.value)

