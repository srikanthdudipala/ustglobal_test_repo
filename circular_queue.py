# circular_queue.py

class CircularQueue:
    def __init__(self, max_length=5):
        self.queue = {}
        self.max_length = max_length

    def enqueue(self, item):
        if len(self.queue) == self.max_length:
            self.dequeue()
        self.queue[len(self.queue) + 1] = item

    def dequeue(self):
        if self.queue:
            self.queue.pop(1)

    def display(self):
        print(list(self.queue.values()))
