def solutionX(s):
    s = list(s.split())
    arr = ""
    for i in range(len(s)):
        for j in range(len(s[i])):
            if (j%2) == 0:
                arr += s[i][j].upper()
            elif (j%2) == 1:
                arr += s[i][j].lower()
        arr += " "
    return arr[:-1]

def solution(s):
    arr = ""
    s = list(s)
    count = 0
    for i in range(len(s)):
        if s[i] == " ":
            count = 0
            arr += " "
        else:
            arr += s[i].upper() if (count%2)==0 else s[i].lower()
            count += 1
    return arr

s = "a bDedf c d e "
print(solution(s))
