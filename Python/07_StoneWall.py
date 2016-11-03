def solution(H):
    if not H:
        return 0
    stack = [H[0]]
    drop = 0
    for i in range(1, len(H)):
        if H[i - 1] == H[i]:
            continue
        elif H[i - 1] < H[i]:
            stack.append(H[i] - H[i - 1])
        else:
            while True:
                p = stack.pop()
                drop += 1
                if H[i - 1] - p < H[i]:
                    stack.append(H[i] - (H[i - 1] - p))
                    break
                elif H[i - 1] - p == H[i]:
                    break
                else:  # H[i - 1] - p > H[i]
                    H[i - 1] -= p
    return len(stack) + drop


if __name__ == '__main__':
    print(solution([2, 3, 2, 1]))
    print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))
