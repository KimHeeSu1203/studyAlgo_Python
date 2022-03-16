N = int(input())
for i in range(N):
    arr = list(map(int,input().split()))
    arr = sorted(arr)
    print(arr[-3])
