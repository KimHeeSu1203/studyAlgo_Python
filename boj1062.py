 ##어떤 알파벳을 가르쳐야 가장 많은 단어를 읽을 수 있을 것인지?
 #하나라도 모르면 그 단어를 못읽는 것임
 #각 단어에 알파벳 갯수 센 다음 가장 적은 알파벳부터 가르쳐야 한다
#antatica -> a,c,t,i,n 은 무조건 가르쳐야된다는 것

## -> 현재
n, k = map(int,input().split())
arr = [set(input()) for _ in range(n)]
arr_len = [len(arr[i]) for i in range(n)]
sum = 0
# for i in range(n):
#     tmp_sum = 0
#     if arr_len[i] == k :
#         for arrJ in arr:
#             if (arr[i] - arrJ) == set(): # 다른 문자열인데 알파벳이 모두 포함되어있으면?
#                 tmp_sum+=1
#     elif arr_len[i] < k :
#         for arrJ in arr:
#             if arr[i]
#     if sum<tmp_sum:
#         sum = tmp_sum
#
# print(sum)
print(set().union(arr[1], arr[2]))

## 변경 -> arr_len의 길이 순서대로 sort를 한 다음에 합집합의 수가 적은 갯수만큼...??
arr.sort(key=len)
for i in range(n):
    tmp_alpha = arr[i]
    for j in range(n):
        if len(tmp_alpha) < k:
            tmp_alpha = tmp_alpha + arr[i+1]
            print(tmp_alpha)
