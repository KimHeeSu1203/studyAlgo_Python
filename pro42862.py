def solution3(n, lost, reserve):
    all_user = [0 for _ in range(n)]
    for i in range(len(lost)):
        all_user[lost[i]-1] += -1

    print(all_user)
    for i in range(len(reserve)):
        all_user[reserve[i]-1] += 1
    print(all_user)
    for i in range(n-1):
        if (all_user[i] + all_user[i+1]) == 0 :
            all_user[i] = 0
            all_user[i+1] = 0
    print(all_user)
    answer = 0

    for i in range(n):
        if (all_user[i] >= 0):
            answer += 1
    #print(all_user,"all")
    return answer

def solution1(n,lost,reserve):
    _reserve = sorted([r for r in reserve if r not in lost])
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

def solution2(n, lost, reserve): ## 틀림
    answer = n-len(lost)
    for i in lost:
        if i in reserve:
            reserve.pop(reserve.index(i)) ## 내가 잃어버리면 내가 메꿔야 함
            lost.pop()

    tmp_lost = []
    for i in lost: ## 빌려줄 수 있는 체육복
        if i-1 > 0:
            tmp_lost.append(i-1)
        if i < n:
            tmp_lost.append(i+1)

    tmp_lost = set(tmp_lost) #
    #lost = set(lost)
    reserve = set(reserve)
    print(tmp_lost)
    print(tmp_lost & reserve)
    answer += len(tmp_lost & reserve) if len(tmp_lost&reserve) <= len(lost) else len(lost)

    return answer


n = 5
lost = [2,3,4]
reserve = [1,2,3]
print(solution1(n,lost,reserve))
