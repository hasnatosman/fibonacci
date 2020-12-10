def find_fib(n):
    if n <= 2:
        return 1
    a, b = 1, 1

    i = 3
    while i <= n:
        i += 1
        a, b = b, a + b
    return b


def list_fib(n):
    l = [1, 1]
    if n <= 2:
        return l[:n]
    a, b = 1, 1

    i = 3
    while i <= n:
        i += 1
        a, b = b, a + b
        l.append(b)
    return l


for x in range(1, 11):
    print(find_fib(x))
print(list_fib(1))
print(list_fib(2))
print(list_fib(3))
print(list_fib(10))
