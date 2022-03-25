def solution(numbers, hand):
    result = []
    startL = 10
    startR = 12

    for i in numbers:

        if i == 0:
            i = 11
        if i in [1,4,7]:
            result.append("L")
            startL = i
        elif i in [3,6,9]:
            result.append("R")
            startR = i
        else:
            # 1번 풀이
            #diffR = abs(i//3-(startR//3 if startR%3 !=0 else startR//3-1)) + abs(((i%3) if (i%3) != 0 else 3) - ((startR%3) if (startR%3) != 0 else 3))
            #diffL = abs(i//3-(startL//3 if startL%3 !=0 else startL//3-1)) + abs(((i%3) if (i%3) != 0 else 3) - ((startL%3) if (startL%3) != 0 else 3))
            # 1(0,1) 2(0,2) 3(0,3) => 이렇게 하지말고 차라리 모든 값을 1씩 뺏으면 훨씬 쉬웠을텐데...
            # 4(1.1) 5(1.2) 6(1.3)
            # 7(2,1) 8(2,2) 9(2,3)
            # 2번 풀이
            tmp_i = i - 1
            tmp_startR = startR-1
            tmp_startL = startL-1
            diffR = abs(tmp_i//3-tmp_startR//3) + abs(tmp_i%3 - tmp_startR%3 )
            diffL = abs(tmp_i//3-tmp_startL//3) + abs(tmp_i%3 - tmp_startL%3)


            if diffL > diffR:
                result.append("R")
                startR = i

            elif diffL < diffR :
                result.append("L")
                startL = i

            elif diffL == diffR:
                if hand == 'right':
                    result.append("R")
                    startR = i
                else:
                    result.append("L")
                    startL = i

    return ''.join(result)






##문제점 : 5에서 시작 시 2로 가나 4, 6으로 가나 똑같은데 그걸 계산해두지 않았음
def wrongSolution(numbers, hand):
    result = []
    startL = '10'
    startR = '12'
    for i in numbers:
        print("------")
        print(" StartL",startL,"StartR",startR, i)
        if i == 0:
            i = 11
        if i in [1,4,7]:
            result.append("L")
            startL = i
        elif i in [3,6,9]:
            result.append("R")
            startR = i
        else:
            if abs(startL - i) > abs(startR - i):
                result.append("R")
                startR = i

            elif abs(startL - i) < abs(startR - i) :
                result.append("L")
                startL = i

            elif abs(startL - i) == abs(startR - i):
                if hand == 'right':
                    print(i)
                    result.append("R")
                    startR = i
                else:
                    print(i)
                    result.append("L")
                    startL = i

            # 1 2 3
            # 4 5 6
            # 7 8 9
    print(len(result))
    return ''.join(result)

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers,hand))
