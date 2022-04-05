def solution(x):
    print(sum(map(int,list(str(x)))))
    return True if x % sum(map(int,list(str(x)))) == 0 else False

def solution2(x):
    return x%sum([int(i) for i in str(x)]) == 0

print(solution2(11))
