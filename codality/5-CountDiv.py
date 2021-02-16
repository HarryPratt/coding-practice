# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, B, K):
    # write your code in Python 3.6
    total = 0
    first = A + ((K - A) % K)
    if first <= B:
        total += 1
    last = B - ((B - K) % K)
    if last == first:
        return total
    elif last - first < 0:
        return total
    else:
        return total + ((last - first) // K)


print(solution(10, 10, 5))
