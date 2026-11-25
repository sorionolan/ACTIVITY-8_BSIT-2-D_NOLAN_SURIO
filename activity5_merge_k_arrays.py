def heapify_up(heap, index):
    while index > 0:
        parent = (index - 1) // 2

        if heap[index] < heap[parent]:
            heap[index], heap[parent] = heap[parent], heap[index]
            index = parent
        else:
            break


def heapify_down(heap, index):
    size = len(heap)

    while True:
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < size and heap[left] < heap[smallest]:
            smallest = left

        if right < size and heap[right] < heap[smallest]:
            smallest = right

        if smallest == index:
            break

        heap[index], heap[smallest] = heap[smallest], heap[index]
        index = smallest


def heap_insert(heap, value):
    heap.append(value)
    heapify_up(heap, len(heap) - 1)


def heap_extract(heap):
    if not heap:
        return None

    if len(heap) == 1:
        return heap.pop()

    minimum = heap[0]
    heap[0] = heap.pop()
    heapify_down(heap, 0)

    return minimum


def merge_k_sorted_arrays(arrays):
    min_heap = []

    # Insert first element of each array
    for i in range(len(arrays)):
        if arrays[i]:
            heap_insert(min_heap, (arrays[i][0], i, 0))

    result = []

    while min_heap:
        value, array_index, element_index = heap_extract(min_heap)

        result.append(value)

        next_index = element_index + 1

        if next_index < len(arrays[array_index]):
            next_value = arrays[array_index][next_index]

            heap_insert(
                min_heap,
                (next_value, array_index, next_index)
            )

    return result


arrays = [
    [1, 4, 7, 10],
    [2, 5, 8],
    [3, 6, 9, 12, 15]
]

print("MERGE K SORTED ARRAYS")
print("Input Arrays:", arrays)

merged = merge_k_sorted_arrays(arrays)

print("Merged Array:", merged)
print("Is Fully Sorted:", merged == sorted(merged))
