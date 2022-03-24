def solution(new_id):
    #1단계
    new_id = new_id.lower()
    new_id = list(new_id)

    #2단계
    for i in range(len(new_id)-1,-1,-1):
        if not (new_id[i].isalpha()) | (new_id[i].isnumeric()) | (new_id[i] in ['-','_','.']):
            new_id.pop(i)

    #3단계
    for i in range(len(new_id)-1,0,-1):
        if (new_id[i] == '.') & (new_id[i-1] == '.'):
            new_id.pop(i)

    #4단계
    if new_id[0] == '.':
        new_id.pop(0)
    if (len(new_id)>0):
        if (new_id[-1] == '.'):
            new_id.pop(-1)

    #5단계
    if len(new_id) == 0:
        new_id.append('a')

    #6단계
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id.pop(-1)


    print(new_id)
    #7단계
    if len(new_id)<3:
        new_id.append(new_id[-1]*(3-len(new_id)))

    return ''.join(new_id)


new_id = "abcdefghijklmn.p"
print(solution(new_id))
