def heapify(arr, n, index):
    largest = index

    left = 2 * index + 1
    right = 2 * index + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]

        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]

        heapify(arr, i, 0)

    return arr


print("HEAP SORT")

test_arrays = [
    [4, 10, 3, 5, 1],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [4, 2, 4, 1, 2],
    []
]

for arr in test_arrays:
    print("Original:", arr)
    print("Sorted:", heap_sort(arr.copy()))
    print()
