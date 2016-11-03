def solution(K, M, A):
    lo = max(A)
    hi = sum(A)

    while lo <= hi:
        mid = (lo + hi) // 2
        if vaild(K, A, mid):
            hi = mid - 1
        else:
            lo = mid + 1

    return lo


def vaild(K, A, mid):
    s = 0
    n = 0
    for i in range(len(A)):
        if s + A[i] > mid:
            s = A[i]
            n += 1
        else:
            s += A[i]
        if n >= K:
            return False
    return True

if __name__ == '__main__':
    print(solution(3, 5, [2, 1, 5, 1, 2, 2, 2]))
    print(solution(1, 10, [5, 3]))
