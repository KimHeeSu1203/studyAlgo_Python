nanjange = []
for i in range(9):
    nanjange.append(int(input()))

sumNanjange10 = sum(nanjange)
notNanjange2 = sumNanjange10 - 100

a, b = 0, 0
for i in range(len(nanjange)):
    for j in range(i):
        if (i != j) & (nanjange[i]+nanjange[j] == notNanjange2):
            a = i
            b = j

nanjange.pop(a)
nanjange.pop(b)

nanjange = sorted(nanjange)
for i in nanjange:
    print(i)

## 전부 다 더한 다음에 100을 넘는 만큼의 무게인 2명을 찾으면 된다

