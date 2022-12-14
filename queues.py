from collections import deque
from dataclasses import dataclass
from heapq import heapify, heappop, heappush
from itertools import count
from typing import Any

#Refactoring the Code Using a Mixin Class
class IterableMixin:
    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()
            
#Building a Queue Data Type
class Queue(IterableMixin):
    def __init__(self, *elements):
        self._elements = deque(elements)

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

#Building a Stack Data Type
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

#Building a Priority Queue Data Type
class PriorityQueue(IterableMixin):
    def __init__(self):
        self._elements = []
        self._counter = count()

    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)

    def dequeue(self):
        return heappop(self._elements)[-1]

@dataclass(order=True)
class Element:
    priority: float
    count: int
    value: Any

class MutableMinHeap(IterableMixin):
    def __init__(self):
        super().__init__()
        self._elements_by_value = {}
        self._elements = []
        self._counter = count()

    def __setitem__(self, unique_value, priority):
        if unique_value in self._elements_by_value:
            self._elements_by_value[unique_value].priority = priority
            heapify(self._elements)
        else:
            element = Element(priority, next(self._counter), unique_value)
            self._elements_by_value[unique_value] = element
            heappush(self._elements, element)

    def __getitem__(self, unique_value):
        return self._elements_by_value[unique_value].priority

    def dequeue(self):
        return heappop(self._elements).value

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
# fruits = []
# heappush(fruits, "orange")
# heappush(fruits, "apple")
# heappush(fruits, "banana")

# print(fruits)

#Popping an element from a heap
# fruits = []
# heappush(fruits, "orange")
# heappush(fruits, "apple")
# heappush(fruits, "banana")

# print(heappop(fruits))

# print(fruits)

# Tuple comparison
# person1 = ("John", "Brown", 42)
# person2 = ("John", "Doe", 42)
# person3 = ("John", "Doe", 24)

# print(person1 < person2)
# print(person2 < person3)

#Priority Queue Test
# CRITICAL = 3
# IMPORTANT = 2
# NEUTRAL = 1

# messages = PriorityQueue()
# messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
# messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
# messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
# messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

# print(messages.dequeue())

# #making the priority a negative number to make the highest one becomes the lowest
# CRITICAL = 3
# IMPORTANT = 2
# NEUTRAL = 1

# messages = PriorityQueue()
# messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
# messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
# messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
# messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

# print(messages.dequeue())
# print(messages.dequeue())
# print(messages.dequeue())
# print(messages.dequeue())