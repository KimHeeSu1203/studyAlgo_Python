def solution(s):
    s = list(s)
    s.sort(reverse=True)
    return "".join(s)

s = "Zbcdefg"
print(solution(s))