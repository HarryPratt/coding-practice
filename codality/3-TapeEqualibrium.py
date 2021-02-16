# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    start = 0
    end = sum(A)
    for i in range(len(A) - 1):
        start += A[i]
        end -= A[i]
        diff = abs(end - start)
        if i == 0:
            min_diff = diff
        else:
            if diff < min_diff:
                min_diff = diff
    return min_diff


print(solution([3, -3]))
