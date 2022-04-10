## 진도 100이면 서비스에 반영, 뒤에 기능이 먼저 개발될수도 있고 앞에 기능이 배포될 떄 함께 배포
#

def solutionX(progresses, speeds):
    count = []
    while(len(progresses)):
        print(progresses, count)
        tmp_num= 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses[0] >= 100:
            progresses.pop(0)
            tmp_num += 1

        if tmp_num>0:
            count.append(tmp_num)

    return count

def solutionX2(progress, speeds):
    arr = []
    while(sum(arr) != len(progress)):
        num = 0
        for i in range(len(progress)):
            progress[i] += speeds[i]
        while(progress[num] > 100):
            num += 1
        arr.append(num)
        print(arr)
    return arr

def getTrueFalse(progress):
    # 전부다 100을 넘기면 전체 길이를 반환해주고
    # 아니면 100 넘기는 길이까지만 반환해주는 함수
    for i in range(len(progress)):
        if progress[i] < 100:
            return i
    return len(progress)

def solution(progress, speeds):
    answer = []
    while(getTrueFalse(progress) != len(progress)) : ## 전부다 100이 넘을 때 까지 # True인 동안 돌아간다
        for i in range(len(progress)):
            progress[i] += speeds[i]
        num = getTrueFalse(progress)
        if (num > 0) & ((num-sum(answer)) > 0):
            answer.append(num-sum(answer))
    return answer
progresses=[95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses,speeds))
