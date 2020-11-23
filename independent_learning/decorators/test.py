#!/usr/bin/env python3
import concurrent.futures
import time

class Dec:
    def __init__(self, number):
        self.number = number
        print(self.number)

    def iter(self, n):
        n.thread_test()
        print("helO")
        print(n)
        time.sleep(n)

        return f"Done sleeping for {n} seconds."

    def thread_test(self):
        print("*" * 72) 
        with concurrent.futures.ThreadPoolExecutor() as executor:
            secs = self.number # [0.5, 1, 0.3, 2]
            [executor.submit(iter, sec) for sec in secs]
            # results = executor.submit(iter, 5) 
        print("_" * 72)

if __name__ == "__main__":
    a = Dec([1, 2, 1])
    a.thread_test()
