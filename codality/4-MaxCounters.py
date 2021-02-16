# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N, A):
    # write your code in Python 3.6
    result = [0] * N
    maxi = 0
    mini = 0
    for i in range(len(A)):
        if A[i] == N + 1:
            mini = maxi
        else:
            if result[A[i] - 1] < mini:
                result[A[i] - 1] = mini + 1
            else:
                result[A[i] - 1] += 1
            if result[A[i] - 1] > maxi:
                maxi = result[A[i] - 1]
    for i in range(len(result)):
        if result[i] < mini:
            result[i] = mini
    return result


print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
