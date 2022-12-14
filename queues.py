from collections import deque

class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()
            
    def __init__(self):
        self._elements = deque()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()
    
    
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

#TEST

#Test FIFO queue
fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

print(fifo.dequeue())
print(fifo.dequeue())
print(fifo.dequeue())

