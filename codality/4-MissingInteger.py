# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    count = []
    for i in range(len(A)):
        if A[i] > (len(count)):
            count.extend([False] * (A[i] + 1 - (len(count))))
        if A[i] > 0 and not count[A[i] - 1]:
            count[A[i] - 1] = True
    for i in range(len(count)):
        if not count[i]:
            return i + 1
    return 1


print(solution([1]))
