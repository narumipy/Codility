def solution(S):
    s = []
    d = {')': '(', ']': '[', '}': '{'}
    for i in range(len(S)):
        if S[i] in d:
            if not s or s.pop() != d[S[i]]:
                return 0
        else:
            s.append(S[i])
    return 0 if s else 1

if __name__ == '__main__':
    print(solution("[[[["))
    print(solution(")("))
    print(solution("{[()()]}"))
    print(solution("([)()]"))
