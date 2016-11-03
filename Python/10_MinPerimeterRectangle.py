def solution(N):
    res = 4 * N
    A = 1
    while A * A <= N:
        if N % A == 0:
            B = N // A
            res = min(res, 2 * (A + B))
        A += 1
    return res

print(solution(30))
