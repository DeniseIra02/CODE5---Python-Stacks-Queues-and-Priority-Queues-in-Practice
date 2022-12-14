from collections import deque
from heapq import heappush, heappop

#Building a Queue Data Type
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

#Building a Stack Data Type
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

#TEST

#Test FIFO queue
# fifo = Queue()
# fifo.enqueue("1st")
# fifo.enqueue("2nd")
# fifo.enqueue("3rd")

# print(fifo.dequeue())
# print(fifo.dequeue())
# print(fifo.dequeue())

#Test (class by making it iterable)
# fifo = Queue()
# fifo.enqueue("1st")
# fifo.enqueue("2nd")
# fifo.enqueue("3rd")

# print(len(fifo))

# for element in fifo:
#     print(element)

# print(len(fifo))

#test LIFO stack
# lifo = Stack()
# lifo.enqueue("1st")
# lifo.enqueue("2nd")
# lifo.enqueue("3rd")

# for element in lifo:
#     print(element)

#Using a Python list as a rudimentary stack
# lifo = []

# lifo.append("1st")
# lifo.append("2nd")
# lifo.append("3rd")

# print(lifo.pop())
# print(lifo.pop())
# print(lifo.pop())

#Representing Priority Queues With a Heap
fruits = []
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

print(fruits)

#Popping an element from a heap
fruits = []
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

print(heappop(fruits))

print(fruits)