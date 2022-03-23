h,w = map(int,input().split())
# board = [ 0 for _ in range(w)]
height = list(map(int, input().split()))
print(height)

## 다음 칸과의 차이만큼

sum = 0

## 물이 고이려면 양옆에 자신보다 높은 불럭이 있어야 하고, 고일 경우 그 고이는 양은 덜 낮은 블록과의 차이만큼

for i in range(1,w-1):
    left_max = max(height[:i])
    right_max = max(height[i+1:])

    compare = min(left_max,right_max)
    if height[i] < compare:
        sum += compare - height[i]

print(sum)


# for i in range(1,w-1): ## 물이 고이려면
#     ## 절댓값의 차이가 나면 빗물 고이는 것
#     print("------------")
#     print(i)
#     if abs(height[flag] - height[i]) > 0 :
#         print(abs(height[flag] - height[i]))
#         if height[flag] != 0:
#             sum += abs(height[flag] - height[i])
#         print(i, flag ,sum )
#     else:
#         flag = i
#         print(i, flag ,sum )
