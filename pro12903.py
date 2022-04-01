def solution(s):
    ##  qwer len(4)
    ##  0123  1:3
    ## abcde len(5)
    ## 01234  2:3

    if len(s) % 2 == 0: # 짝수면
        return s[len(s)//2-1: len(s)//2+1]
    else:
        return s[len(s)//2]

s = "qwer"
print(solution(s))