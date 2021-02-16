# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N):
    # write your code in Python 3.6
    binary_gap = 0
    count = 0
    for character in bin(N)[2:]:
        if character == "1":
            if count > binary_gap:
                binary_gap = count
            count = 0
        elif character == "0":
            count += 1
    return binary_gap


for inp in [1041, 15, 32]:
    print(solution(inp))
