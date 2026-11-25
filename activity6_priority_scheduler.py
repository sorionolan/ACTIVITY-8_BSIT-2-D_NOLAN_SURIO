class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, job):
        self.heap.append(job)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index][0] > self.heap[parent][0]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

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

            if left < size and self.heap[left][0] > self.heap[largest][0]:
                largest = left

            if right < size and self.heap[right][0] > self.heap[largest][0]:
                largest = right

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

    def size(self):
        return len(self.heap)


def priority_scheduler(jobs):
    priority_queue = MaxHeap()

    # Add jobs to priority queue
    for priority, job_name in jobs:
        priority_queue.insert((priority, job_name))

    release_order = []

    while priority_queue.size() > 0:
        job = priority_queue.extract()
        release_order.append(job)

    return release_order


jobs = [
    (2, "Job A"),
    (5, "Job B"),
    (1, "Job C"),
    (4, "Job D"),
    (3, "Job E")
]

print("PRIORITY SCHEDULER")
print("Jobs:", jobs)

schedule = priority_scheduler(jobs)

print("\nRelease Order:")

for priority, job_name in schedule:
    print(f"Priority {priority}: {job_name}")
