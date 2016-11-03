def solution(A, B):
    up_stream = []
    down_stream = []
    for i in range(len(A)):
        cur_size = A[i]
        cur_dir = B[i]
        if cur_dir == 0:
            if len(up_stream) == 0:
                down_stream.append(cur_size)
            else:
                while up_stream:
                    up_stream_size = up_stream.pop()
                    if up_stream_size > cur_size:
                        up_stream.append(up_stream_size)
                        break
                if not up_stream:
                    down_stream.append(cur_size)
        else:
            up_stream.append(cur_size)
    return len(up_stream) + len(down_stream)


if __name__ == '__main__':
    print(solution([0, 1], [1, 1]))
    print(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))
