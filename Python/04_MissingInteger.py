def solution(A):
    m = 1
    s = set()
    for a in A:
        if a > 0:
            s.add(a)
    while m:
        if m in s:
            m += 1
        else:
            return m

if __name__ == '__main__':
    print(solution([1, 3, 6, 4, 1, 2]))
