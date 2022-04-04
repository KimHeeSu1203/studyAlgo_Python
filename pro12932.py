def solution(n):
    n = list(str(n))
    n.reverse()
    return list(map(int,n))

print(solution(12345))
