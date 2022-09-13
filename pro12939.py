def solution(s):
    answer = list(map(int,s.split()))
    tmp_answer = str(min(answer)) + " " + str(max(answer))
    return tmp_answer

print(solution("-1 -2 -3 -4"))
