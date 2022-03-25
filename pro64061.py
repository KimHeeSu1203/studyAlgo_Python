def solution(board, moves):
    reverseBoard = [[] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 0:
                reverseBoard[j].append(board[i][j])

    result = []
    pop = 0
    result.append(reverseBoard[moves[0]-1].pop(0))
    for i in moves[1:]:
        if len(reverseBoard[i-1])>0:
            result.append(reverseBoard[i-1].pop(0))
            if result[-1] == result[-2]:
                result.pop()
                result.pop()
                pop += 2
    return pop


board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board,moves))
