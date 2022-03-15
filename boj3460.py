"""
양의 정수 n이 주어졌을 때,
이를 이진수로 나타냈을 때 1의 위치를 모두 찾는 프로그램을 작성하시오. 최하위 비트(least significant bit, lsb)의 위치는 0이다.
"""

def solution(n):
    arr = []
    while(n != 0):
        arr.append(n%2)
        n = n//2

    for i in range(len(arr)):
        if arr[i] == 1:
            print(i, end = ' ')

T = int(input())
for t in range(T):
    n = int(input())
    solution(n)
