class Node():
    def __init__(self):
        self.prev = None
        self.next = None
        self.stack = []


class SetOfStacks:    # c3 q3
    def __init__(self, t):
        self.head = None
        self.tail = None
        self.length = 0
        self.threshold = t

    def push(self, el):
        curr = self.head
        while curr and len(curr.stack) == self.threshold:
            curr = curr.next

        if curr:
            curr.stack.append(el)
        else:
            node = Node()
            node.stack.append(el)

            if self.length:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            else:
                self.head = node
            self.tail = node
            self.length += 1

    def pop(self):
        curr = self.tail
        if curr:
            el = curr.stack.pop(-1)
            if len(curr.stack) == 0:
                if self.length == 1:
                    self.head = None
                    self.tail = None
                else:
                    curr.prev.next = None
                    self.tail = curr.prev
                self.length -= 1
            return el

    def print(self):
        curr = self.head
        while curr:
            print('Stack:', curr.stack)
            curr = curr.next


s = SetOfStacks(3)
for i in range(8):
    s.push(i)
print(s.pop())
s.print()
