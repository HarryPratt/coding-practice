# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(X, A):
    # write your code in Python 3.6
    count = [1] * X
    uncovered = X
    for i in range(len(A)):
        if count[A[i] - 1] != 0:
            count[A[i] - 1] = 0
            uncovered -= 1
            if uncovered == 0:
                return i
    return -1


print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
