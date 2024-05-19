# sum of 1 to n
def sum(n, s):
    if n < 1:
        print(s)
        return
    sum(n - 1, s + n)


# sum(5, 0)


# using functional recursion
def sum_(n):
    if n == 0:
        return 0
    return n + sum_(n - 1)


# print(sum_(5))


# factorial
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


print(fact(6))


# TC --> O(n)
# SC --> O(n)
