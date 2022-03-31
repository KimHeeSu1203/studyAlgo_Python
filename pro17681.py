def make2num(n,arr1):
    answer = []
    for i in arr1:
        tmp_answer = []
        while(i):
            tmp_answer.append(i%2)
            i = i // 2
        while(len(tmp_answer)<n):
            tmp_answer.append(0)
        tmp_answer.reverse()
        answer.append(tmp_answer)
    return answer

def solution(n,arr1,arr2):
    arr1Map = make2num(n,arr1)
    arr2Map = make2num(n,arr2)
    totalMap = ["" for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr1Map[i][j] + arr2Map[i][j] == 0:
                totalMap[i] += ' '
            else:
                totalMap[i] += "#"
    return totalMap


n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
print(solution(n,arr1, arr2))