def solution(x):
    print(sum(map(int,list(str(x)))))
    return True if x % sum(map(int,list(str(x)))) == 0 else False


print(solution(11))
