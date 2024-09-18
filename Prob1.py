import heapq

# Problem 1: Merge K sorted arrays
def merge_k_sorted_arrays(arrays):
    heap = []
    result = []
    
    # Insert the first element of each array into the heap
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))  # (value, array index, element index)
    
    # Extract the minimum element from the heap and add the next element of the array to the heap
    while heap:
        val, arr_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        # If the current array has more elements, add the next one to the heap
        if elem_idx + 1 < len(arrays[arr_idx]):
            heapq.heappush(heap, (arrays[arr_idx][elem_idx + 1], arr_idx, elem_idx + 1))
    
    return result

# Example usage
if __name__ == "__main__":
    array1 = [1, 3, 5, 7]
    array2 = [2, 4, 6, 8]
    array3 = [0, 9, 10, 11]
    arrays = [array1, array2, array3]

    print("Merged array:")
    merged_array = merge_k_sorted_arrays(arrays)
    print(merged_array)
