def solution(a, b):
    answer = sum([x for x in range(a, (b+1) if a<=b else (b-1),1 if a<=b else -1)])
    return answer

a = 3
b = 5
print(solution(a,b))