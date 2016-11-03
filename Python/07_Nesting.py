def solution(S):
    if not S:
        return 1
    if S[0] == ")":
        return 0
    stack = [S[0]]
    for i in range(1, len(S)):
        if S[i] == "(":
            stack.append("(")
        else:  # S[i] == ")"
            if stack:
                stack.pop()
            else:
                return 0
    if stack:
        return 0
    return 1

if __name__ == '__main__':
    print(solution(")()"))
    print(solution(""))
    print(solution("()()(())"))
    print(solution("(()(())())"))
    print(solution("())"))
