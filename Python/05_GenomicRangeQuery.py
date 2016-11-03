def solution(S, P, Q):
    d = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    s = [d[S[i]] for i in range(len(S))]
    areas = [gen(s, i) for i in range(1, len(d) + 1)]
    res = [0] * len(P)
    for i in range(len(P)):
        for j in range(len(areas) - 1, -1, -1):
            x = areas[j][P[i]]
            if x >= 0 and x - (Q[i] - P[i]) >= 0:
                res[i] = j + 1
                break
    return res


def gen(s, x):
    res = [-1] * len(s)
    c = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] < x:
            c = 0
        else:
            c += 1
            res[i] += c
    return res

if __name__ == '__main__':
    print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))
