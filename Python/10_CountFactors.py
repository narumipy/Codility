def solution(N):
    if not N > 0:
        return 0
    res = 0
    i = 1
    while i * i < N:
        if N % i == 0:
            res += 2
        i += 1

    if i * i == N:
        res += 1

    return res