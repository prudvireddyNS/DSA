def selectionSort(arr, n):
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


def bubbleSort(arr, n):
    for i in range(n - 1):
        didSwap = 0
        for j in range(n - 1 - i):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                didSwap = 1
        if didSwap == 0:
            break


def insertionSort(arr, n):
    for i in range(1, n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
         

def mergeSort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)
    merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    for i in range(len(temp)):
        arr[low + i] = temp[i]


def quickSort(arr, low, high):
    if low < high:
        pi = partitionIndex(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def partitionIndex(arr, low, high):
    p = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < p:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def run_tests_from_file(file_path, test_function):
    with open(file_path, "r") as file:
        num_cases = int(file.readline().strip())
        for _ in range(num_cases):
            n = int(file.readline().strip())
            arr = list(map(int, file.readline().strip().split()))
            try:
                test_function(arr, n)
                print(f"The result is: {arr}")
            except ValueError as e:
                print(e)


if __name__ == "__main__":
    # For merge and quick sort
    # arr = [1, 9, 5, 5, 3, 5, 6]
    # mergeSort(arr, 0, 6)
    # print(arr)

    # for selection, bubble and insertion sort
    # test_file = "test.txt"
    # run_tests_from_file(test_file, insertionSort)

    pass
