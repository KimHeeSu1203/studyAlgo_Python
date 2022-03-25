def solution(s):
    alphaDict = {
        'zero' : '0' ,
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }

    for alpha in alphaDict.keys():
        if alpha in s:
            s = s.replace(alpha,alphaDict[alpha])

    return int(s)


s ="one4seveneight"
print(solution(s))
