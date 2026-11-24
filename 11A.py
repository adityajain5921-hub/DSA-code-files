def max_heapify(arr, heap_size, root_index):
    """Maintain the max-heap property for subtree rooted at root_index."""
    largest = root_index
    left = 2 * root_index + 1
    right = 2 * root_index + 2

    # Check if left child exists and is greater than root
    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    # If root is not the largest, swap and continue heapifying down
    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]
        max_heapify(arr, heap_size, largest)


def heap_sort_ascending(arr):
    n = len(arr)

    # Step 1: Build a max-heap from the bottom up
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

    # Step 2: Extract elements one by one from the heap
    for end in range(n - 1, 0, -1):
        # Move current largest (at index 0) to the end of unsorted portion
        arr[0], arr[end] = arr[end], arr[0]
        # Restore max-heap property on the reduced heap
        max_heapify(arr, end, 0)

    return arr


# --- Example Usage ---
numbers_asc = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", numbers_asc)
sorted_asc = heap_sort_ascending(numbers_asc.copy())
print("Sorted (Ascending):", sorted_asc)