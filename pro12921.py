import math
def solution(n):
    answer = 0
    #answer = set()
    if n == 1:
        return 0

    for i in range(2,n+1): ## 2부터 모든 수까지
        flag = True
        for j in range(2,int(math.sqrt(n))+1):
            if (i%j == 0) & (i!=j):
                flag = False
                break #한번이라도 0 이 되면 i 자체를 그만
        if flag == True:
            answer += 1
    return answer

## 효율성 없음
def solutionX(n):
    answer = 0

    for i in range(n+1):
        tmpList= []
        for j in range(1,i+1):
            if i%j == 0:
                tmpList.append(j)
        if len(tmpList) == 2:
            print(tmpList)
            answer += 1

    return answer

n = 10
print(solution(n))