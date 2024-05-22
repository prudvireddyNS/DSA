# Reverse an array
def reverse(i, ar, n):
    if i >= n / 2:
        return
    ar[i], ar[n - i - 1] = ar[n - i - 1], ar[i]
    reverse(i + 1, ar, n)


ar = [1, 2, 3, 4, 5]
reverse(0, ar, 5)
print(ar)


# palindrome
def palindrome(i, s):
    if i >= len(s) // 2:
        print("True, It's a Palindrome")
        return
    if s[i] != s[len(s) - i - 1]:
        print("False, Not a Palindrome")
        return
    palindrome(i + 1, s)


s = "madam"
palindrome(0, s)


# Fibonacci
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(6))
