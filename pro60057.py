## 같은 값이 연속해서 나ㅌ타나는 것을 줄이고 싶은 것
# 압축해서 표현한 것 중 가장 짧은 것의 길이를 return

def solution(s):
    # count = 1
    arr = []
    answer = []
    # for i in range(1, len(s)):
    #     if s[i-1] == s[i]:
    #         count += 1
    #     else:
    #         arr.append(s[i-1])
    #         if count != 1:
    #             arr.append(str(count))
    #         count = 1
    # arr.append(s[-1])
    # arr.append(str(count))

    tmp_arr = []
    count = 1
    if len(s)== 1:
        return 1
    for j in range(1,len(s)//2+1): # 단위, j == 1 이면 한칸씩 비교, 0~j, j+
        tmp_arr = []
        for i in range(0,len(s),j):
            print(s[i:i+j],s[i+j:i+2*j]) # 0:0+1 ,0+1 : 0+2
            if s[i:i+j] == s[i+j:i+2*j]:
                count +=1
            else:
                tmp_arr.append(s[i:i+j])
                if count != 1:
                    tmp_arr.append(str(count))
                count = 1
        print("".join(tmp_arr))
        arr.append(len("".join(tmp_arr)))
    print(arr)
    return min(arr)


s = "a"
print(solution(s))
