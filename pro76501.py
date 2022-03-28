def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] *= -1
    return sum(absolutes)

absolutes = [4,7,12]
signs = [True,False,True]

print(solution(absolutes,signs))