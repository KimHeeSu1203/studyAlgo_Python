def solution(p,k):
    arr = []
    for i in range(1,p+1):
        if (p % i) == 0:
            arr.append(i)
            if len(arr) == k:
                return arr[-1]
    return 0
p, k = map(int, input().split())
print(solution(p,k))



