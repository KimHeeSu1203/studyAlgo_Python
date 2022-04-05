def solution(n,m):
    arr = []
    arr_tmp = []
    for i in range(1,min(n,m)+1):
        if (n%i == 0) & (m%i == 0):
            arr.append(i)
    print(max(arr))
    return [max(arr), max(arr) *(n//max(arr)) * (m//max(arr))]


# 정확도 75/100
def solutionX1(n, m):
    n = min(n,m)
    m = max(n,m)
    arr_n = set()
    arr_m = set()
    for i in range(1,n+1):
        if n%i==0:
            arr_n.add(i)

    for i in range(1,m+1):
        if m%i==0:
            arr_m.add(i)

    print(arr_n, arr_m)
    max_num = max(arr_n&arr_m)
    i = 1
    while(1):
        i = i+1
        if (max_num*i % n == 0) & (max_num*i % m == 0):
            return [max_num,max_num*i]

    # print(arr_n, arr_m)
    # print(max(arr_n&arr_m)) #교집합
    # print(arr_n&arr_m) #교집합
    # print(arr_n | arr_m) #합집합


def solutionX(n,m):
    arr = [1,1]
    i = 1
    while(1):
        i = i+1
        if (n%i == 0) & (m%i == 0):
            arr[1] *= i
            n = n % i
            m = m % i


n = 3
m = 12

print(solution(n,m))
