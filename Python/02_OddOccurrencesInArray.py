def solution(A):
    r = 0
    for x in A:
        r ^= x
    return r

if __name__ == '__main__':
    print(solution([1, 2, 1, 2, 3]))
