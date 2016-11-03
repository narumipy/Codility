def solution(A):
    d = {}
    m = 0
    res = -1
    for i in range(len(A)):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1

        if d[A[i]] > m:
            m = d[A[i]]
        if d[A[i]] > len(A) / 2:
            res = i
    return res

if __name__ == '__main__':
    print(solution([3, 4, 3, 2, 3, -1, 3, 3]))
