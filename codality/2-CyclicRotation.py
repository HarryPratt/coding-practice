# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, K):
    # write your code in Python 3.6
    if len(A) == 0:
        return A
    remainder = K % len(A)
    front = A[-remainder:]
    back = A[:-remainder]
    A_new = front + back
    return A_new


tests = [([3, 8, 9, 7, 6], 3), ([0, 0, 0], 1), ([1, 2, 3, 4], 4)]
for inp in tests:
    print(solution(A=inp[0], K=inp[1]))
