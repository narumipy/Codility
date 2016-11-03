def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def solution(N, M):
    d = gcd(N, M)
    return N / d
