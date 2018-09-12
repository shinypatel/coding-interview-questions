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
        return self.stack[-1]

    def min(self):  # q2
        if self.min:
            return self.min

    def print(self):
        for el in self.stack:
            print(el)


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
