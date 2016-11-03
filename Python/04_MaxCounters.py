def solution(N, A):
    res = [0] * N
    cur_m = 0
    pre_m = 0
    for a in A:
        if a == N + 1:
            pre_m = cur_m
        else:
            if res[a - 1] < pre_m:
                res[a - 1] = pre_m
            res[a - 1] += 1
            cur_m = max(res[a - 1], cur_m)
    for i in range(N):
        res[i] = max(res[i], pre_m)
    return res


if __name__ == '__main__':
    print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
