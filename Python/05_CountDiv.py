def solution(A, B, K):
    r = A % K
    if r:
        A += r
    return (B - A) // K + 1

if __name__ == '__main__':
    print(solution(6, 11, 2))
    print(solution2(6, 11, 2))
