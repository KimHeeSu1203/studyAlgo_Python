def solution(strings, n):
    #strings.sort(keambda )
    strings.sort(key = lambda x:(x[n],x))
    return strings

strings = ["sun", "bed", "car"]
n = 1
print(solution(strings,n))