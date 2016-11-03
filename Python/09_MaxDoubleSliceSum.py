def solution(A):
    # Kadane's algorithm
    l = [0] * len(A)
    r = [0] * len(A)

    for i in range(1, len(A) - 1):
        l[i] = max(0, l[i - 1] + A[i])
    for i in range(len(A) - 2, 0, -1):
        r[i] = max(0, r[i + 1] + A[i])

    res = 0
    for i in range(1, len(A) - 1):
        res = max(res, l[i - 1] + r[i + 1])
    return res

if __name__ == '__main__':
    print(solution([5, 17, 0, 3]))
    print(solution([3, 2, 6, -1, 4, 5, -1, 2]))
