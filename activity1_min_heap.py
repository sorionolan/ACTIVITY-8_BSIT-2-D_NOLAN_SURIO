class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def extract(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        minimum = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return minimum

    def heapify_down(self, index):
        size = len(self.heap)

        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    def size(self):
        return len(self.heap)


min_heap = MinHeap()

numbers = [5, 9, 11, 14, 19, 17, 18, 13]

for number in numbers:
    min_heap.insert(number)

print("MIN-HEAP")
print("Heap:", min_heap.heap)
print("Peek:", min_heap.peek())
print("Size:", min_heap.size())

print("Extract order:", end=" ")

while min_heap.size() > 0:
    print(min_heap.extract(), end=" ")

print()
