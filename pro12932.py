def solution(n):
    n = list(str(n))
    n.reverse()
    return list(map(int,n))

def solution2(n):
    return list(map(int,reversed(str(n))))
print(solution2(12345))
