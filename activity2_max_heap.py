class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] > self.heap[parent]:
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

        maximum = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return maximum

    def heapify_down(self, index):
        size = len(self.heap)

        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left

            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

    def size(self):
        return len(self.heap)


max_heap = MaxHeap()

numbers = [5, 9, 11, 14, 19, 17, 18, 13]

for number in numbers:
    max_heap.insert(number)

print("MAX-HEAP")
print("Heap:", max_heap.heap)
print("Peek:", max_heap.peek())
print("Size:", max_heap.size())

print("Extract order:", end=" ")

while max_heap.size() > 0:
    print(max_heap.extract(), end=" ")

print()
