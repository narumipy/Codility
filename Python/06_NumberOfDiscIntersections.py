def solution(A):
    left = [i - A[i] for i in range(len(A))]
    right = [i + A[i] for i in range(len(A))]
    pairs = sorted(zip(left, right))
    res = 0
    for i in range(len(A)):
        lo = i + 1
        hi = len(A) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if pairs[mid][0] > pairs[i][1]:
                hi = mid - 1
            else:
                lo = mid + 1
        res += lo - i - 1
        if res > 10000000:
            return -1
    return res

if __name__ == '__main__':
    print(solution([1, 5, 2, 1, 4, 0]))
