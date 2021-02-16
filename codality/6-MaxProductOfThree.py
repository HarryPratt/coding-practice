# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    A.sort()
    if len(A) == 3:
        return A[0] * A[1] * A[2]
    else:
        return max(
            A[0] * A[1] * A[-1],
            A[1] * A[2] * A[-1],
            A[0] * A[1] * A[2],
            A[-1] * A[-2] * A[-3],
        )


print(solution([-10, -2, -4]))
