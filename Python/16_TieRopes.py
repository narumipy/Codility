def solution(K, A):
    total = 0
    l = [0] * len(A)
    for i in range(len(A)):
        l[i] = l[i - 1] + A[i] if i > 0 else A[i]

        if l[i] >= K:
            total += 1
            l[i] = 0
    return total
