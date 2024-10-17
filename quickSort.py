def quick_sort(arr):
    """Main function to perform quick sort"""
    if len(arr) <= 1:  # Base case: arrays of length 0 or 1 are already sorted
        return arr
    
    pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot
    
    # Recursively sort the left and right partitions and combine them
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Original array:", arr)
    
    sorted_arr = quick_sort(arr)
    print("Sorted array:", sorted_arr)
