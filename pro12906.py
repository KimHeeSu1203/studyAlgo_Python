def solution(arr):
    answer = [arr[0]]
    print(answer)
    for i in arr[1:]:
        if i != answer[-1]:
            answer.append(i)

    return answer


arr = [1,1,3,3,0,1,1] ## 연속되어있는 경우만
print(solution(arr))