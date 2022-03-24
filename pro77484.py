def solution(lottos, win_nums):
    num0 = lottos.count(0)
    lottos = set(lottos)
    win_nums = set(win_nums)
    answer = []
    #겹치는거
    # 1등 6개/ 2등 5개/ 3등 4개/ 4등 3개/ 5등 2개/ 6등 나머지
    # 겹치는 숫자 - 0의 갯수?

    yesAnswer = len(win_nums & lottos)
    #noAnswer = len(win_nums-lottos)
    # 높은 등수 : 맞은거 갯수 + 0의 갯수 - 틀린거 갯수   가 내가 맞을 수 있는
    # 낮은 등수 : 맞은거 갯수

    answer.append(7-yesAnswer-num0 if 7-yesAnswer-num0 != 7 else 6)
    answer.append(7-yesAnswer if 7-yesAnswer != 7 else 6)

    return answer

def solution2(lottos,win_nums):
    rank = [6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0

    for x in win_nums:
        if x in lottos:
            ans += 1

    return rank[cnt_0+ans],rank[ans]

lottos = [1, 2, 3, 4, 5, 6]
win_nums = 	[38, 19, 20, 40, 15, 25]
print(solution(lottos,win_nums))
print(solution2(lottos,win_nums))
