#!/usr/bin/sudo python

"""
Hello Robin! Welcome!

Fibonacci sequence is a sequence of numbers where 1st is 0 and 2nd elements is 1 and every other element is a sum of two previous ones. Write fib(k) -- a function returning k-th element from Fibonacci sequence (starting with 0)

0, 1, 1, 2, 3, 5, 8, 13, 21, 34

fib(1) = 0
fib(2) = 1
fib(3) = 1
fib(4) = 2
etc. etc.

1. Write a function that returns the kth element of the Fibonacci sequence
[as above]

2.
3rd: 0,0,1,1,2,4,7,13,24,44,81,149
trib(1) = 0
trib(2) = 0
trib(3) = 1
trib(4) = 1
trib(5) = 2 etc.BaseException
"""


def fib(k):
    if k == 1 or k == 0:
        return 0
    elif k == 2:
        return 1
    else:
        return fib(k - 1) + fib(k - 2)


def trib(k):
    trib = [0, 0, 1]
    for i in range(2, k):
        trib.append(sum(trib[-3:]))
    return trib[k - 1]


## Endo-nacci Function
def endonacci(k, n):
    endo = [0] * (n - 1)
    endo.append(1)
    for i in range(n - 1, k):
        endo.append(sum(endo[-n:]))
    return endo[k - 1]


if __name__ == "__main__":
    # print(fib(2))
    # print(fib(6))
    # print(fib(8))

    # print(trib(4))
    # print(trib(6))
    # print(trib(7))
    # print(trib(1))

    print(endonacci(4, 3))
    print(endonacci(5, 2))
    print(endonacci(6, 4))
