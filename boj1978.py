N = int(input())
arr = list(map(int, input().split()))
count = N

for i in arr:
    if i == 1:
        count = count -1
    elif (i!=2):
        for j in range(2,i):
            if (i%j) == 0:
                ## 소수 아님
                count = count - 1
                break
print(count)

