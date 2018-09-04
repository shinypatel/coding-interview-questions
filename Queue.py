class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, el):
        self.queue.append(el)

    def dequeue(self):
        if self.queue:
            el = self.queue[0]
            del self.queue[0]
            return el
