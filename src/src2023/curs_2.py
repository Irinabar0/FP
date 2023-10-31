
def fib(n: int) -> int:

    """"
    Calculate the n-th term of the Fibonacci sequence

    :param n: the index of the term
    :return: The term's value
    """

    # 1. Base case, we break recursion
    if n < 2:
        return n
    # 2. Progress towards the base case
    return fib(n - 2) + fib(n - 1)


#def fib // copy his repository

#assert fib(i) == fib_iter(i), (i, fib(i), fib_iter(i)) returns AssertionError: (0,0,1) if it's False,
# at the call of test_fib(10)


#print(fib(5000))