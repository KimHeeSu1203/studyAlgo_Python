def cal(now,arr,num,a,b,c,d):
	if a>0:
		cal(now+arr[num],arr,num+1,a-1,b,c,d)
	if b>0:
		cal(now-arr[num],arr,num+1,a,b-1,c,d)
	if c>0:
		cal(now*arr[num],arr,num+1,a,b,c-1,d)
	if d>0:
		cal(int(now/arr[num]),arr,num+1,a,b,c,d-1)
	if (a+b+c+d) == 0:
		answer.append(now)



N = int(input())
arrA = list(map(int,input().split()))
a,b,c,d = map(int,input().split())
answer = []
cal(arrA[0],arrA,1,a,b,c,d)

print(max(answer))
print(min(answer))
