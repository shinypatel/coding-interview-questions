def bubble_sort(arr):
    swapped = False
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            swapped = True
    if swapped:
        arr = bubble_sort(arr)
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(0, n):
        smallest, idx = float('inf'), None
        for j in range(i, n):
            if arr[j] < smallest:
                smallest, idx = arr[j], j
        del arr[idx]
        arr.insert(i, smallest)
    return arr


# https://stackoverflow.com/questions/18761766/mergesort-python
def merge(arr1, arr2):
    result = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    return result + arr1[i:] + arr2[j:]


def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    m = int(n / 2)
    arr1 = merge_sort(arr[:m])
    arr2 = merge_sort(arr[m:])
    return merge(arr1, arr2)





a = [5, 4, 3, 2, 1]
print(merge_sort(a))
