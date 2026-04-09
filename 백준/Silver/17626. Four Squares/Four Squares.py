import math

n = int(input())

answer = 0

def solution(n):
    # a^2
    if math.isqrt(n) ** 2 == n:
        print(1)
        return

    # a^2 + b^2
    for a in range(math.isqrt(n), 0, -1):
        if n - a ** 2 == math.isqrt(n - a ** 2) ** 2:
            print(2)
            return

    # a^2 + b^2 + c^2
    for a in range(math.isqrt(n), 0, -1):
        for b in range(math.isqrt(n - a ** 2),0,-1):
            if n - a ** 2 - b ** 2== math.isqrt(n - a ** 2 - b ** 2) ** 2:
                print(3)
                return

    # a^2 + b^2 + c^2 + d^2
    print(4)
    return

solution(n)