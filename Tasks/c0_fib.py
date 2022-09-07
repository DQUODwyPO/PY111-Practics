def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError("Fibonacci ValueError: n < 0")
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError("Fibonacci ValueError: n < 0")
    fibs = [0, 1]
    size = 2
    while n >= size:
        fibs.append(fibs[size-1] + fibs[size-2])
        size += 1
    return fibs[n]
