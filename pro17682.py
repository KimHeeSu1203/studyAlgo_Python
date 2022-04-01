"""
다트 게임은 총 3번의 기회로 구성된다.
각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
"""

def solution(dartResult):
    flag = 0
    dartResult = dartResult
    tmpdart = []
    for i in range(len(dartResult)):
        if (dartResult[i].isnumeric() == False) & (dartResult[i] not in ["#",'*']):
            tmpdart.append(dartResult[flag:i]) ## 숫자가 아니면 묶
            tmpdart.append(dartResult[i])
            flag = i+1
        elif dartResult[i] in ["#",'*']:
            tmpdart.append(dartResult[i])
            flag += 1

    print(tmpdart)

    for i in range(len(tmpdart)-1, -1, -1):
        if tmpdart[i] == 'D':
            tmpdart[i-1] =  pow(int(tmpdart[i-1]),2)
            tmpdart.pop(i)
        elif tmpdart[i] == 'T':
            tmpdart[i - 1] = pow(int(tmpdart[i - 1]), 3)
            tmpdart.pop(i)
        elif tmpdart[i] == 'S':
            tmpdart[i-1] = int(tmpdart[i-1])
            tmpdart.pop(i)
    print(tmpdart)
    ## * 2번 연속 오는 경우가 해결이 안되고 있음
    for i in range(len(tmpdart)-1,-1,-1):
        if (tmpdart[i] == '*') & (i == 1):
            tmpdart[i-1] = tmpdart[i-1]*2
            tmpdart.pop(i)
        elif (tmpdart[i] == '*') & (i != 1):
            tmpdart[i-1] = tmpdart[i-1] * 2
            if tmpdart[i-2] not in ['*','#']:
                tmpdart[i-2] = tmpdart[i-2] * 2
            else:
                tmpdart[i - 3] = tmpdart[i - 3] * 2
            tmpdart.pop(i)
        elif tmpdart[i] == '#':
            tmpdart[i-1] = tmpdart[i-1] * -1
            tmpdart.pop(i)
    print(tmpdart)
    return sum(tmpdart)

## 10같이 두자리인 경우 해결을 못했음
def solution2(dartResult):
    tmpDart = []
    dartResult = list(dartResult)
    flag = 0
    for i in range(1,len(dartResult)):
        if dartResult[i] in ["0","1","2","3","4","5","6","7","8","9","10"]:
            tmpDart.append(dartResult[flag:i])
            flag = i
    tmpDart.append(dartResult[flag:])
    print(tmpDart)

    for i in range(len(tmpDart)):
        if (tmpDart[i][0] == '1') & (tmpDart[i][1] == '0'):
            tmpDart[i].pop(0)
            tmpDart[i][0]=10
        num = int(tmpDart[i][0])

        if tmpDart[i][1] == 'D':
            num = pow(num,2)
        elif tmpDart[i][1] == 'T':
            num = pow(num,3)
        tmpDart[i] = [num,(tmpDart[i][2] if len(tmpDart[i]) > 2 else 0)]
    print(tmpDart)
    answer = 0

    for i in range(len(tmpDart)):
        if len(tmpDart[i]) > 1:
            if (tmpDart[i][1] == '*') & (i==0):
                tmpDart[i][0] = int(tmpDart[i][0]) * 2
            elif (tmpDart[i][1] == '*') & (i>0):
                tmpDart[i-1][0] = int(tmpDart[i-1][0]) * 2
                tmpDart[i][0] = int(tmpDart[i][0]) * 2
            elif (tmpDart[i][1] == '#'):
                tmpDart[i][0] = int(tmpDart[i][0]) * -1

    print(tmpDart)
    for a,b in tmpDart:
        answer += a

    return answer

dartResult = "1S*2T*3S"
print(solution(dartResult))

