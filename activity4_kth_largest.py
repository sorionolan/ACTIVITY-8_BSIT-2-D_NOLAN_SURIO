class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1

        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def extract(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        minimum = self.heap[0]
        self.heap[0] = self.heap.pop()

        index = 0
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

        return minimum

    def size(self):
        return len(self.heap)

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]


def kth_largest(numbers, k):
    if k < 1 or k > len(numbers):
        return None

    min_heap = MinHeap()

    for number in numbers:
        min_heap.insert(number)

        if min_heap.size() > k:
            min_heap.extract()

    return min_heap.peek()


numbers = [3, 2, 1, 5, 6, 4]
k = 2

print("KTH LARGEST")
print("Numbers:", numbers)
print("K:", k)

result = kth_largest(numbers, k)

print("Kth Largest:", result)
print("Sorted Verification:", sorted(numbers, reverse=True)[k - 1])
