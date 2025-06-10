# Mahid Mohammadi khah 982011056

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def get_size(self):
        return len(self.queue)

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False


size = int(input())
queue = Queue()
for s in range(size):
    queue.enqueue(input())

print(queue.get_size())
print(queue.is_empty())
print(queue.dequeue())