def solution(A):
    dp = [A[0]] * 6
    for i in range(1, len(A)):
        dp[i % 6] = max(dp) + A[i]
    return dp[(len(A) - 1) % 6]

if __name__ == '__main__':
    print(solution([0, -4, -5, -2, -7, -9, -3, -10]))
