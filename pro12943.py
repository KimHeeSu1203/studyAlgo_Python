def solution(num):
    cnt = 0
    #        1
    while((num!=1) & (cnt!= 500)): # 여기가 0이 되어야 중단하는 것 둘중의 하나만 0이어도 중단해야하는 것 -> 1이거나, 카운트가 500이면 그만   | (cnt<= 500)
        cnt += 1
        if num%2 == 0:
            num = num//2
        else:
            num = num*3 + 1

    if num == 1:
        return cnt
    else:
        return -1

print(solution(626331))

"""
1-1. 입력된 수가 짝수라면 2로 나눕니다. 
1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
"""
