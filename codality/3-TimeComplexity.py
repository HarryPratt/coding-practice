# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(X, Y, D):
    # write your code in Python 3.6
    distance_req = Y - X
    if distance_req % D == 0:
        return int(distance_req / D)
    else:
        return (distance_req // D) + 1
