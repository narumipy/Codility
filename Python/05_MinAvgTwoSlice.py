def solution(A):
    m = float("inf")
    idx = -1
    for i in range(len(A) - 1):
        s = (A[i] + A[i + 1]) / 2.0
        if s < m:
            m = s
            idx = i
    for i in range(len(A) - 2):
        s = (A[i] + A[i + 1] + A[i + 2]) / 3.0
        if s < m:
            m = s
            idx = i
    return idx


if __name__ == '__main__':
    print(solution([4, 2, 2, 5, 1, 5, 8]))
    print(solution([0, 15, 16, 15, 7]))
