def solution(id_list, report, k):
    answer_num = [0 for _ in range(len(id_list))]
    answer_name = [[] for _ in range(len(id_list))]
    answer = [0 for _ in range(len(id_list))]
    report = set(report)

    for i in report:
        a,b = i.split(' ')
        answer_num[id_list.index(b)] += 1
        answer_name[id_list.index(b)].append(a)

    for i in range(len(answer_num)):
        if answer_num[i] >= k:
            for j in range(len(answer_name[i])):
                answer[id_list.index(answer_name[i][j])] += 1
    return answer

#한번에 한명 신고 가능
#여러번 신고도 가능하지만 동일한 유저에 대해선 1번으로 친다
#k번 이상 신고되면 정지되고 메일로 받는다
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

print(solution(id_list, report, k))
