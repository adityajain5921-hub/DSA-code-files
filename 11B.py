def min_heapify(arr, heap_size, root_index):
    """Maintain the min-heap property for subtree rooted at root_index."""
    smallest = root_index
    left = 2 * root_index + 1
    right = 2 * root_index + 2

    # Check if left child exists and is smaller than root
    if left < heap_size and arr[left] < arr[smallest]:
        smallest = left

    # Check if right child exists and is smaller than current smallest
    if right < heap_size and arr[right] < arr[smallest]:
        smallest = right

    # If root is not the smallest, swap and continue heapifying down
    if smallest != root_index:
        arr[root_index], arr[smallest] = arr[smallest], arr[root_index]
        min_heapify(arr, heap_size, smallest)


def heap_sort_descending(arr):
    n = len(arr)

    # Step 1: Build a min-heap from the bottom up
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)

    # Step 2: Extract elements one by one from the heap
    for end in range(n - 1, 0, -1):
        # Move current smallest (at index 0) to the end of unsorted portion
        arr[0], arr[end] = arr[end], arr[0]
        # Restore min-heap property on the reduced heap
        min_heapify(arr, end, 0)

    return arr


# --- Example Usage ---
numbers_desc = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", numbers_desc)
sorted_desc = heap_sort_descending(numbers_desc.copy())
print("Sorted (Descending):", sorted_desc)