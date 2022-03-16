num = list(map(int, input().split()))
## 최대공약수
a = min(num)
b = max(num)
for i in range(a,0,-1):
    if ((a%i)==0) & ((b%i)==0):
        print(i)
        break

## 최소공배수 24, 18이면 작은거에 곱을 해서
print(int(a*b/i))


#tmp = 1
# while(1):
#     if ((a*tmp)%b) == 0:
#         print(a*tmp)
#         break
#     else:
#         tmp = tmp+1
