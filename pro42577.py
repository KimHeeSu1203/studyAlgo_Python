# 구조대 전화번호는 영석이 전화번호 접두사
# 다른 번호의 접두어인 경우 있으면 false 아니면 true
def solution(phone_book):
    phone_book.sort(key=lambda x:(x,len(x)))

    for i in range(len(phone_book)-1):
        #print(phone_book[i],phone_book[i+1][:len(phone_book[i])])
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False

    return True

phone_book = ["12","123","1235","567","88"]
print(solution(phone_book))




def solutionEX(phone_book):
    answer = True
    phone_book.sort(key=lambda x: (x,len(x)))
    print(phone_book)
    for k in range(len(phone_book)-1):
        if phone_book[k] in phone_book[k+1]:
            answer = False

    return answer

