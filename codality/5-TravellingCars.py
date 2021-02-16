def solution(A):
    # write your code in Python 3.6
    pre = [0] * len(A)
    for i in range(len(A)):
        if i == 0:
            pre[-i - 1] = A[-i - 1]
        else:
            pre[-i - 1] = pre[-i] + A[-i - 1]
    total = 0
    for i in range(len(A)):
        if A[i] == 0:
            total += pre[i]
    if total > 1000000000:
        return -1
    else:
        return total


print(solution([0, 1, 0, 1, 1]))
