def solution(A):
    d = {}
    for i in range(len(A)):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1

    e = {}
    m = 0
    m_idx = -1
    res = 0
    for i in range(len(A) - 1):
        if A[i] in d:
            d[A[i]] -= 1
            if d[A[i]] == 0:
                del d[A[i]]

        if A[i] in e:
            e[A[i]] += 1
        else:
            e[A[i]] = 1

        if e[A[i]] > m:
            m = e[A[i]]
            m_idx = i

        if m > (i + 1) / 2.0:
            if A[m_idx] in d and d[A[m_idx]] > (len(A) - i - 1) / 2.0:
                res += 1
    return res

if __name__ == '__main__':
    print(solution([3, 4, 3, 2, 3, -1, 3, 3]))
    print(solution([4, 3, 4, 4, 4, 2]))
