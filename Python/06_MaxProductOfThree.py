def solution(A):
    a = sorted(A)
    l = a[:3]
    for i in range(3):
        if len(a) - 1 - i > 2:
            l.append(a[len(a) - 1 - i])
    m = float("-inf")
    for i in range(len(l)):
        for j in range(len(l)):
            for k in range(len(l)):
                if (i - j) * (i - k) * (j - k):
                    m = max(m, l[i] * l[j] * l[k])
    return m

if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(solution([10, 10, 10]))
    print(solution([4, 5, 1, 0]))
