def makePM(arr,idx):
    if idx == (len(arr) -1) :
        return

def solution(numbers, target):
    ## +, - 로 numbers를 ....
    numbers.insert(0,0)
    print(numbers)
    answer = makePM(numbers,0)


    return



numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))
