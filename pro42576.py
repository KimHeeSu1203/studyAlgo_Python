def solution1(participant, completion):
    for i in range(len(completion)):
        participant.pop(participant.index(completion[i]))
    print(participant)

def solution2(participant, completion):
    for i, name in enumerate(participant):
        if name not in completion:
            return name
        else:
            participant.pop(i)


def solution3(participant, completion):
    participant.sort()
    completion.sort()
    print(participant)
    print(completion)
    for a,b in zip(participant,completion):
        print(a,b)
        if a != b:
            return a
    return participant[-1]


participant =["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution3(participant,completion))



