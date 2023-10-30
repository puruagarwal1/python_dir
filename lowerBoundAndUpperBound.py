def lower_bound(array, X):
    low = 0
    high = len(array) - 1

    while low < high:
        mid = (low + high) // 2

        if X <= array[mid]:
            high = mid
        else:
            low = mid + 1

    if low < len(array) and array[low] < X:
        low += 1

    return low

def upper_bound(array, X):
    low = 0
    high = len(array) - 1

    while low < high:
        mid = (low + high) // 2

        if X >= array[mid]:
            low = mid + 1
        else:
            high = mid

    if low < len(array) and array[low] <= X:
        low += 1

    return low


def print_bound(array, X):
    lower_bound_index = lower_bound(array, X)
    upper_bound_index = upper_bound(array, X)

    if lower_bound_index == len(array):
        print("Lower bound doesn't exist")
    else:
        print("Lower bound of {} is {} at index {}".format(X, array[lower_bound_index], lower_bound_index))

    if upper_bound_index == len(array):
        print("Upper bound doesn't exist")
    else:
        print("Upper bound of {} is {} at index {}".format(X, array[upper_bound_index], upper_bound_index))


array = [2, 8, 22, 34, 35, 100, 107, 208]

X = 22
print_bound(array, X)
X = 43
print_bound(array, X)
X = 107
print_bound(array, X)

