arr = [0,1]
N = int(input())

while(len(arr)<=N):
    arr.append(arr[-1]+arr[-2])

print(arr[N])
