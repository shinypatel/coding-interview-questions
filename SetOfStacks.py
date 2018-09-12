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


    def pop_at(self, idx):
        curr = self.head
        for i in range(1, idx + 1):
            if curr:
                curr = curr.next

        if curr:
            el = curr.stack.pop(-1)
            if len(curr.stack) == 0:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next

                if curr.next:
                    curr.next.prev = curr.prev
                else:
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
print(s.pop_at(0))
s.print()
