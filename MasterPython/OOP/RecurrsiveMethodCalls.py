# a recursive method can take a lot longer to execute as it has to keep calling itself during runtime

# a recursive function is one which might include itself
# a factorial i the product of an integer and all the integers below it; e.g. factorial four ( 4! ) is equal to 24.
# 5 = 5*4*3*2*1 = 120
# for any value of n, n factorial can be calculated by itself * result of itself - 1 n -1
# ie. 5 factorial is the result of 4 factorial * 5 (24*5=120)

def fact(n):
    # calculates n! interatively
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    # calculates n! recursively
    # can also be defined as n * (n-1)! - 5 * 4 factorial ( 5 * 24)
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def fib(n):
    # f(n) = f(n-1) + f(n-2)
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n_minus_1 = 1
        n_minus_2 = 0
        for f in range(1, n):
            result = n_minus_2 + n_minus_1
            n_minus_2 = n_minus_1
            n_minus_1 = result
    return result

for i in range(36):
    print(i, fibonnaci(i))