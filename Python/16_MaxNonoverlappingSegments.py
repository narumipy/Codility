def solution(A, B):
    if not A:
        return 0
    total = 1
    a = A[-1]
    b = B[-1]
    for i in range(len(A) - 2, -1, -1):
        if a <= A[i] <= b or a <= B[i] <= b:
            if A[i] > a:
                a = A[i]
                b = B[i]
        else:
            total += 1
            a = A[i]
            b = B[i]

    return total

if __name__ == '__main__':
    print(solution([], []))
    print(solution([1, 3, 7, 9, 9], [5, 6, 8, 9, 10]))
