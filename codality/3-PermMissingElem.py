# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    sum = (len(A) + 1) * (len(A) + 2)
    expected_sum = int(sum / 2)
    new_sum = 0
    for i in range(len(A)):
        new_sum += A[i]
    return expected_sum - new_sum


print(solution([2, 3, 1, 5]))
