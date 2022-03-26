
def solution(nums):
    sosu = []

    for i in range(2,1000+999+998):
        flag = False
        for j in range(2,i):
            if i%j == 0:
                flag = True
                break
        if flag == False:
            sosu.append(i)

    answer = 0
    for i in nums:
        for j in nums[nums.index(i)+1:]:
            for k in nums[nums.index(j)+1:]:
                if (i + j + k) in sosu:
                    answer += 1

    return answer


nums = [1,2,7,6,4]
print(solution(nums))