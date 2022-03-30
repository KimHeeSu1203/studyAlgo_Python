## 최대한 많은 부서 지원해주려고 한다 -> 작은 금액부터 지원해주는 것이 좋을 듯

def solution(d,budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        if sum(d[:i+1]) <= budget:
            answer += 1
        else:
            break

    return answer


d = [1,3,2,5,4]
budget = 9
print(solution(d,budget))