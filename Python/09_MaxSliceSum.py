def solution(A):
    if not A:
        return
    res = float("-inf")
    pre = float("-inf")
    for a in A:
        pre = max(pre + a, a)
        res = max(pre, res)
    return res

if __name__ == '__main__':
    print(solution([0]), 0)
    print(solution([1]), 1)
    print(solution([-10]), -10)
    print(solution([1, 1]), 2)
    print(solution([1, 1, 2]), 4)
    print(solution([-2, 1]), 1)
    print(solution([-3, -2, -3, -2]), -2)
    print(solution([3, 2, -6, 4, 0]), 5)
