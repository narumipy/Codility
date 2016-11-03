def solution(A, K):
    if not A or not K:
        return A
    return [A[(i - K) % len(A)] for i in range(len(A))]

if __name__ == '__main__':
    print(solution([3, 8, 9, 7, 6], 3))
