"""
섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
k 이상 될때까지 반복
"""

import heapq
def solutionHeapQ(scoville, K):
    answer = 0
    scoville.sort()

    while(scoville[0])<K:
        if len(scoville)<=1:
            return -1
        else:
            small = heapq.heappop(scoville)
            small2 = heapq.heappop(scoville)
            heapq.heappush(scoville, (small + (small2 * 2))) ## 최솟값이 제일 앞으로 자동으로 오게 된다
            answer += 1
    return answer



def check(scoville, K):
    for i in scoville:
        if i < K:
            return False
    return True

def solution(scoville,K):
    # tmp = [lambda x : x > K for x in scoville]
    # print(tmp)
    # print(all([lambda x : x > K for x in scoville]))
    cnt = 0
    scoville.sort()
    while(not check(scoville,K)):
        if (len(scoville) == 1) & (scoville[0]<K):
            return -1
        elif (len(scoville) == 1) & (scoville[0]>=K):
            return 0
        cnt +=1
        print(scoville)
        scoville[1] = scoville[0] + (scoville[1] * 2)
        scoville.pop(0)
        scoville.sort()
    return cnt

scoville = [1, 2, 3, 9, 10, 12]
K = 7
#print(solution(scoville,K))
print(solutionHeapQ(scoville,K))
