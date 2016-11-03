def solution(A):
    s = set([i for i in range(1, len(A) + 1)])
    for a in A:
        if a in s:
            s.remove(a)
        else:
            return 0
    if len(s) == 0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    print(solution([4, 1, 3, 2]))
    print(solution([4, 1, 3]))
