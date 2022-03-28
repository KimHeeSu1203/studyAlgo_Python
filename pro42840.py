def solution(answers):
  answer = []
  kk = []
  students = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]


  for student in students:
    tmp_student = student*(len(answers)//len(student)+1)
    tmp_right = 0
    for i in range(len(answers)):
      if answers[i] == tmp_student[i]:
        tmp_right += 1

    kk.append(tmp_right)
  maxAnswer = max(kk)
  for i in range(len(students)):
    if maxAnswer == kk[i]:
        answer.append(i+1)
  return answer
