def solution(arr, divisor):
    answer = []
    for num in arr:
        if num%divisor == 0:
            answer.append(num)
    answer.sort()
    return answer if len(answer) >0 else [-1]
def solution2(arr,division):
    answer = [x for x in arr if x%divisor==0]
    answer.sort()
    return answer if len(answer) != 0 else [-1]

arr = [3,2,6]
divisor = 10
print(solution(arr,divisor))