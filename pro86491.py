def solution(sizes):
    answer = 0
    ## 모든 명함을 작, 큰으로 정렬해서 최댓값을 출력하면 될 듯

    for i in sizes:
        i.sort()
    sizeX = 0
    sizeY = 0

    for a,b in sizes:
        if a > sizeX:
            sizeX = a
        if b > sizeY:
            sizeY = b

    return sizeX * sizeY



sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))