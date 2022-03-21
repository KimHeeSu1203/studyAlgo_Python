# 서로 다른 자연수 N의 합이 S라고 할 때
# 자연수 N의 최대값은 ?
# 최대한많은 수로 N을 만들면 되는 것 -> 즉 작은 수로 만드는게 제일 쉬운 것

S = int(input())
tmpSum = 0
num = 0
for i in range(1,4294967295):
    tmpSum = tmpSum + i
    num = num + 1
    if tmpSum > S:
        break

print(num-1)
