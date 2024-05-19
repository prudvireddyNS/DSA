cnt = 0


# print name 5 times
def printName5times(i, n):
    if i > n:
        return
    print("prudvi")
    printName5times(i + 1, n)


# print 1 to n
def oneToN(i, n):
    global cnt
    if i > n:
        return
    print(i)
    oneToN(i + 1, n)


# print n to 1
def nToOne(i):
    if i < 1:
        return
    print(i)
    nToOne(i - 1)


# print 1 to n using backtracking
def oneToN_b(n):
    if n < 1:
        return
    oneToN_b(n - 1)
    print(n)


# print n to 1 using backtracking
def nToOne_b(i, n):
    if i > n:
        return
    nToOne_b(i + 1, n)
    print(i)


if __name__ == "__main__":
    # printName5times(1, 5)

    # n = int(input("Enter n value: "))
    # oneToN(1, n)

    # n = int(input("Enter n value: "))
    # nToOne(n)

    # n = int(input("Enter n value: "))
    # oneToN_b(n)

    n = int(input("Enter n value: "))
    nToOne_b(1, n)
