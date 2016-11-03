def solution(A):
    if not A:
        return
    if len(A) == 1:
        return 0
    l = 0
    r = sum(A)
    m = float("inf")
    for i in range(1, len(A)):
        l += A[i - 1]
        r -= A[i - 1]
        d = abs(r - l)
        m = min(d, m)
    return m

print(solution([3, 1, 2, 4, 3]))
print(solution([-1000, 1000]))
