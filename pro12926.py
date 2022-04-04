def solution(s, n):
    arr = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")*2
    arr_s = [i.lower() for i in arr]*2
    answer = ""
    for i in s:
        if i in arr:
            answer += arr[arr.index(i)+n]
            ##answer += arr[arr.index(i)+n if arr.index(i)+n < len(arr) else len(arr)-arr.index(i)+n-2]
        elif i in arr_s:
            answer += arr_s[arr_s.index(i)+n]
            ##answer += arr_s[arr_s.index(i)+n if arr_s.index(i)+n < len(arr_s) else len(arr_s)-arr_s.index(i)+n-2]
        else:
            answer += i
    return answer

s = "a B z"
n = 4
print(solution(s,n))

# z = len(arr) -1
# a = 0
# n = 1
#
# len(arr) - (len(arr) -1) + n = n + 1
