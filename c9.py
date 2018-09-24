from random import randint


def bubble_sort(arr):
    swapped = False
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            swapped = True
    if swapped:
        arr = bubble_sort(arr)
    return arr


def selection_sort(arr):    # outer loop - gives pos; inner loop - finds el
    n = len(arr)
    for i in range(n):
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


def merge_sort(arr):    # sort in end
    n = len(arr)
    if n == 1:
        return arr
    m = int(n / 2)
    arr1 = merge_sort(arr[:m])
    arr2 = merge_sort(arr[m:])
    return merge(arr1, arr2)


def quick_sort(arr):    # sort in beginning
    n = len(arr)
    if n == 1:
        return arr
    pivot = int(n / 2)
    for i in range(pivot):
        if arr[i] > arr[pivot]:
            arr.append(arr.pop())
    arr1 = quick_sort(arr[:pivot])
    arr2 = quick_sort(arr[pivot:])
    return arr1 + arr2


def insertion_sort(arr):    # outer loop - gives el; inner loop - finds pos
    n = len(arr)
    for i in range(n):
        for j in range(i):
            if arr[j] > arr[i]:
                arr.insert(j, arr.pop(i))
    return arr


def bucket_sort(arr, m):
    buckets = [[] for b in range(m)]

    x_min, x_max = min(arr), max(arr)
    interval = x_max - x_min
    for x in arr:
        idx = int(((x - x_min) / interval) * (m - 1))
        buckets[idx].append(x)

    result = []
    for b in range(m):
        result += insertion_sort(buckets[b])
    return result
