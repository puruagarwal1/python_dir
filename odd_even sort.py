def odd_even_sort(arr):
    """
    Sorts the array using the Odd-Even Sort (Brick Sort) algorithm.

    Args:
    arr (list): List to be sorted.

    Returns:
    list: Sorted list.

    """
    n = len(arr)
    is_sorted = 0  # Initially set as 0 to enter the loop
    while is_sorted == 0:
        is_sorted = 1  # Assume the list is sorted
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = 0  # If swapping occurs, the list is not sorted
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = 0  # If swapping occurs, the list is not sorted
    return arr


# Example usage
arr = [5, 2, 3, 1, 4]
print("Original array:", arr)
sorted_arr = odd_even_sort(arr)
print("Sorted array:", sorted_arr)
