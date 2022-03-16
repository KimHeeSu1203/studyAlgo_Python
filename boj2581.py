a = int(input())
b = int(input())

smallValue = -1
valueSum = 0

for i in range(b,a-1,-1):
    if i!=1:
        flag = True
        for j in range(2,i):
            if (i%j) == 0: ## 소수 아님
                flag = False
                break
        if flag == True:
            valueSum += i
            smallValue = i

if valueSum != 0:
    print(valueSum)
print(smallValue)
