def fib_test(n):
    a, b = 0, 1
    while a < n:
        print(a, end=',')
        a, b = b, a+b
    print()


fib_test(257)