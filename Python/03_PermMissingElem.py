def solution(A):
    n = len(A)
    s = (n + 1) * (n + 2) / 2
    return s - sum(A)

print(solution([1]))
print(solution([2]))
print(solution([2, 3, 1, 5]))
