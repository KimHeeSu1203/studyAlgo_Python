#튜플

def solution(s):
    listS = s[2:-2].split('},{')
    listS.sort(key=len)

    answer = [int(listS[0])]
    for i in range(1, len(listS)):
        answer.append(int(list(set(listS[i].split(',')) - set(listS[i-1].split(',')))[0]))
    return answer

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))
