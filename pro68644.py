def solution(numbers):
    answer = set()
    for i in range(len(numbers)): ##서로 다른 인덱스에 있는 두 수를 뽑아서 더하는 것
        for j in range(i+1,len(numbers)):
            answer.add(numbers[i]+numbers[j])
    return sorted(list(answer))


numbers = [0,100]
print(solution(numbers))