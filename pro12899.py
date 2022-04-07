def solution(n):
    # 1,2,4,11,12,14,21,22,24
    arr = [1,2,4]
    answer = []
    while(n):
        print(n%3)
        answer.append(arr[n%3-1])
        n = (n-1) // 3

    answer.reverse()
    answer = map(str,answer)
    return "".join(answer)


n = 5
print(solution(n))

"""
0+arr[0]
0+arr[1]
0+arr[2]
1+1 // arr[0]




"""
