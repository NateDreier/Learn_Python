#!/usr/bin/env python3

"""
Playing with Decorators
1. Timing decorator to test the speed of a function.
2. Decorating decorator to decorate the output.
3. Number checking decorator to check the validity of the number. 
"""

import time
import concurrent.futures


def decoratorator(func):
    def p(*args):
        func(*args)
        print("*" * 72)
        print("DONE")

    return p


def timerator(func):
    def f(*args):
        before = time.perf_counter()
        rv = func(*args)
        after = time.perf_counter()
        print(f"Elapsed time: {round(after-before, 2)} ")

    return f


def test_nat_num(func):
    def helper(n):
        if type(n) == int and n > 0:
            return func(n)
        else:
            raise Exception("Argument is not an integer")
    return helper

@test_nat_num
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#print(factorial(4))

@decoratorator
@timerator
def iter(*args):
    time.sleep(*args)

    return f"Done sleeping for {args} seconds."


if __name__ == "__main__":
    @timerator
    def thread_test():
        print("*" * 72)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            secs = [.5, 1, .3, 2]
            [executor.submit(iter, sec) for sec in secs]
        print("_" * 72)

    thread_test()

    print("\nRunning the factorial function")
    print(factorial(4))
