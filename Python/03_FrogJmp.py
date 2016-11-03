def solution(X, Y, D):
    d = (Y - X) // D
    r = (Y - X) % D
    if r == 0:
        return d
    else:
        return d + 1

if __name__ == '__main__':
    print(solution(10, 85, 30))
    print(solution(10, 85, 30))
