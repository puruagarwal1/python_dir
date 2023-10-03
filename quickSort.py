def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    
    swap(arr, i + 1, high)
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

arr = [34, 23, 54, 19, 1, 5]
N = len(arr)

quickSort(arr, 0, N - 1)

print("Sorted array:")
for i in range(N):
    print(arr[i], end=" ")
