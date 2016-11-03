def solution(N):
    if not N:
        return 0
    b = bin(N)[2:]
    res = 0
    cur = 0
    for i in range(1, len(b)):
        if b[i] == '0':
            cur += 1
        else:
            if cur >= res:
                res = cur
            cur = 0
    return res


if __name__ == '__main__':
    print(solution(74901729))
    print(solution(561892))
