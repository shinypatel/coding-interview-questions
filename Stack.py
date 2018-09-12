class Stack:
    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, el):     # q2
        if not self.min or el < self.min:
            self.min = el
        self.stack.append(el)

    def pop(self):
        if self.stack:
            return self.stack.pop(-1)

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def min(self):  # q2
        return self.min

    def is_empty(self):
        if len(self.stack):
            return False
        else:
            return True

    def print(self):
        print(self.stack)


def q1(n):
    arr = []
    for i in range(n):
        arr.append(i)

    s1, s2, s3 = Stack(), Stack(), Stack()
    for i in arr[::3]:
        s1.push(arr[i])
        if i + 2 < len(arr):
            s3.push(arr[i + 2])
            s2.push(arr[i + 1])
        elif i + 1 < len(arr):
            s2.push(arr[i + 1])

    print('stack 1:')
    s1.print()
    print('stack 2:')
    s2.print()
    print('stack 3:')
    s3.print()


def reverse(s1):
    s2 = Stack()
    while s1.peek() is not None:
        s2.push(s1.pop())
    return s2


class Queue:    # q5
    def __init__(self):
        self.queue = Stack()

    def enqueue(self, el):
        self.queue.push(el)

    def dequeue(self):
        self.queue = reverse(self.queue)
        el = self.queue.pop()
        self.queue = reverse(self.queue)
        return el

    def print(self):
        self.queue.print()


def q5():
    q = Queue()
    for j in range(4):
        q.enqueue(j)
    print(q.dequeue())
    q.print()


def sort_stack(s1):   # q6
    s2 = Stack()
    while not s1.is_empty():
        curr = s1.pop()
        s3 = Stack()
        print('s2:')
        s2.print()
        print('s3:')
        # stack s2 is in descending order i.e. [-1, 1]
        while not s2.is_empty():
            prev = s2.pop()
            print('prev:', prev)
            print('curr:', curr)
            # construct stack s3 in ascending order i.e. [1, -1]
            if prev < curr:
                prev, curr = curr, prev
            s3.push(prev)
            s3.print()
        s3.push(curr)
        s3.print()
        print('\n')
        s2 = reverse(s3)
    return s2


s = Stack()
s.push(5)
s.push(0)
s.push(1)
s.push(-1)
s.print()
print('\n\n')
sort_stack(s).print()
