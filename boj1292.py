a, b = map(int,input().split())
arr = []

i = 1
while(len(arr)<=b):
    tmp = [i] * i
    arr.extend(tmp)
    i = i+1

print(sum(arr[a-1:b]))
