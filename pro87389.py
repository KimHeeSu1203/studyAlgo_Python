def solution(n):
    for i in range(1, n):
        if n % i == 1:
            return i


n = 3

print(solution(n))