## 포켓몬 n마리 중 n/2마리
## 최대한 많은 종류의 폰켄몬
def solution(nums):
    answer = len(nums)//2
    #1.
    if len(set(nums)) >= answer:
        return answer
    else:
        return len(set(nums))


nums = [3,3,3,2,2,2]
print(solution(nums))
