from itertools import combinations
def solution(orders, course):
    ## X 주문을 알파벳, 길이 순으로 정렬 -> 2번 이상 주문된 조합으로만 진행
    ## 메뉴 unique로 만들어서 조합으로 그냥 만들면...?
    #orders.sort(key= lambda x : (len(x), x))

    menus = set()
    for order in orders:
        for i in order:
            menus.add(i)
    print(menus)
    all_menus = []
    for i in range(2,len(menus)):
        all_menus.append(list(combinations(menus,i)))
    answer = []
    for menucombi in all_menus:
        count = 0
        for order in orders:
            if menucombi in order:
                count+=1
                if count >= 2:
                    answer.append(menucombi)
                    continue
    print(answer)

    return answer

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders,course))
