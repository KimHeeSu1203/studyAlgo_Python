def solution(s):
    s = list(s)
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 0
    while(len(s)):
        flag = False
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                s.pop(i)
                s.pop(i)
                flag = flag | True
                break
            else:
                flag = flag | False
        if flag == False:
            print(s)
            return 0
    return 1

s = 'aaaaa'
print(solution(s))
