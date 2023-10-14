def get_count(arr, s, e, pivot):
    count = 0

    for i in range(s, e):
        if arr[i] < pivot:
            count += 1

    return count

def partition(arr, s, e):
    pivot = arr[s]
    count = get_count(arr, s, e, pivot)
    pivot_index = s + count

    arr[pivot_index], arr[s] = arr[s], arr[pivot_index]

    i, j = s, e

    while i < pivot_index and j > pivot_index:
        while arr[i] < arr[pivot_index]:
            i += 1

        while arr[j] > arr[pivot_index]:
            j -= 1

        if i < pivot_index and j > pivot_index:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    return pivot_index

def quick_sort(arr, s, e):
    if s >= e:
        return

    p = partition(arr, s, e)

    quick_sort(arr, s, p - 1)
    quick_sort(arr, p + 1, e)

if __name__ == "__main__":
    arr = [234, 432, 234, 231, 12, 432, 1324, 5432, 234, 453]
    
    s, e = 0, len(arr) - 1

    quick_sort(arr, s, e)

    for i in range(len(arr)):
        print(arr[i], end=" ")
