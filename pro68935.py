def solution(n):
    n3num = []
    while(n>0):
        n3num.append(n%3)
        n = n //3

    answer = 0
    for i in range(len(n3num)):
        answer += n3num[i] * (pow(3,len(n3num)-(i+1)))
    return answer


n = 45
#print(solution(n))


## int에는 진수를 변환해주는 기능도 있다
def solution2(n):
    tmp = ''
    while(n):
        tmp+=str(n%3)
        n = n//3

    answer = int(tmp,3)
    print(answer)

solution2(n)