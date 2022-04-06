"""
채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
채팅방에서 닉네임을 변경한다.
닉네임을 변경할 때는 기존에 채팅방에 출력되어 있던 메시지의 닉네임도 전부 변경된다.
중복 닉네임 허용한다
"""
def solution(record):
    answer = {}
    for data in record:
        data = data.split()

        if data[0] == "Enter":
            answer[data[1]] = data[2]
        if data[0] == "Change":
            answer[data[1]] = data[2]

    result = []
    for data in record:
        data = data.split()
        if "Enter" in data:
            result.append(answer[data[1]] + "님이 들어왔습니다.")
        elif "Leave" in data :
            result.append(answer[data[1]] + "님이 나갔습니다.")
    return result



record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
