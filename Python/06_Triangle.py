def solution(A):
    a = sorted(A)
    for i in range(len(a) - 2):
        if a[i] + a[i + 1] > a[i + 2]:
            return 1
    return 0
