#left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.


def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        num = 1
        for j in range(1,i):
            if (i%j) == 0:
                num += 1
        if num % 2 == 0:
            print(i, answer, num)
            answer += i
        else:
            answer -= i

    return answer


left = 1
right = 2
print(solution(left,right))