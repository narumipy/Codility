def solution(A):
    res = 0
    c = 0
    for a in A:
        if a == 0:
            c += 1
        else:
            res += c
            if res > 1000000000:
                return -1
    return res

if __name__ == '__main__':
    print(solution([0, 1, 0, 1, 1]))
