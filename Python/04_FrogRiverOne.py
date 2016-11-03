def solution(X, A):
    d = set([i for i in range(1, X + 1)])
    for i in range(len(A)):
        cur = A[i]
        if cur in d:
            d.remove(cur)
        if len(d) == 0:
            return i
    return -1
print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))

print(solution(5, [1, 1, 1, 1, 1, 1, 1, 1]))
print(solution(5, [1]))