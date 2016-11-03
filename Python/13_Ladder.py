def solution(A, B):
    L = len(A)

    m = max(A) + 1
    ways = [1, 1] + [0] * (m - 2)
    for i in range(2, m):
        ways[i] = ways[i - 1] + ways[i - 2]

    res = []
    for i in range(L):
        res.append(ways[A[i]] % (2**B[i]))
    return res
