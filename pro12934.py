import math
def solution(n):
    num = math.sqrt(n)
    if int(num) == num:
        return int(math.pow(num+1,2))
    else:
        return -1

n=121
print(solution(n))
