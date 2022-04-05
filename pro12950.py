def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr1[0])
    answer = []
    for i in range(n):
        tmp_answer = []
        for j in range(m):
            tmp_answer.append(arr1[i][j] + arr2[i][j])
        answer.append(tmp_answer)
    return answer

arr1 = [[1],[2]]
arr2 = [[3],[4]]

print(solution(arr1, arr2))
