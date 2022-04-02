def solution(s):
    return True if (s.count('P')+s.count('p')) == (s.count('Y')+s.count('y')) else False


s = "pPoooyY"
print(solution(s))