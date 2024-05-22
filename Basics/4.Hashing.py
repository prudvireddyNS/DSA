# to find the count of given number in an array
if __name__ == "__main_":
    n = int(input("Enter len of array"))
    ar = [0] * n
    for i in range(n):
        ar[i] = int(input(f"Enter {i}th element"))

    hash = [0] * len(ar)
    for i in range(len(ar)):
        hash[ar[i]] += 1

    q = int(input("Enter no. of test cases"))
    for i in range(q):
        num = int(input("Enter number to find the count"))
        print(hash[num])

# to find the count of given char in a string
if __name__ == "__main_":
    s = input("Enter a string")
    s = s.lower()

    hash = [0] * 256
    for i in range(len(s)):
        hash[ord(s[i]) - ord("a")] += 1

    q = int(input("Enter no.of test cases: "))
    for i in range(q):
        char = input("Enter the char to find the count")
        print(hash[ord(char) - ord("a")])


# map
if __name__ == "__main__":
    n = int(input("Enter len of array"))
    ar = [0] * n
    for i in range(n):
        ar[i] = int(input(f"Enter {i}th element"))

    map = {}
    for i in range(len(ar)):
        map[ar[i]] = map.get(ar[i], 0) + 1

    q = int(input("Enter no. of test cases"))
    for i in range(q):
        num = int(input("Enter number to find the count"))
        print(map.get(num, 0))
