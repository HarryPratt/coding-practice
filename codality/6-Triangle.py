from collections import deque


def solution(A):
    A.sort()
    if len(A) < 3:
        return 0
    triangle = 0
    triplet = deque([A[0], A[1]])
    for i in range(2, len(A)):
        triplet.append(A[i])
        if (
            triplet[0] + triplet[1] > triplet[2]
            and triplet[2] + triplet[0] > triplet[1]
        ):
            return 1
        triplet.popleft()
    return 0


print(solution([10, 50, 5, 1]))
