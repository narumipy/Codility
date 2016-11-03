def solution(A):
    if not A:
        return 0
    min_price = A[0]
    max_profit = 0
    for i in range(1, len(A)):
        max_profit = max(max_profit, A[i] - min_price)
        min_price = min(min_price, A[i])
    return max_profit

if __name__ == '__main__':
    print(solution([23171, 21011, 21123, 21366, 21013, 21367]))
