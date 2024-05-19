def selectionSort(arr, n):  # TC -> O(n^2)
    for i in range(n - 1):
        mini = i
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                mini = j


def bubbleSort(arr, n):
    for i in range(n - 1, -1, -1):
        didSwap = 0
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                didSwap = 1

        if didSwap == 0:
            break


def insertionSort(arr, n):
    for i in range(n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


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
    test_file = "test.txt"
    run_tests_from_file(test_file, insertionSort)
