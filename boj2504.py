"""
‘()’ 인 괄호열의 값은 2이다.
‘[]’ 인 괄호열의 값은 3이다.
‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.
"""
strArr = list(input())
print(strArr)

# 치환해서 쓰는게 나을지...
# pop해서 쓰는게나을지
tmpStack = []
tmpStack.append(strArr.pop(0))
answerArr = []
answer = 0
# [] -> 3, () -> 2
# [()]

while(len(strArr)>0):
  if (strArr == '['):
    answer = answer * 3
    tmpStack.append(strArr.pop(0))
  elif (strArr[0] == '('):
    answer = answer * 2
    tmpStack.append(strArr.pop(0))
  elif (tmpStack[-1] == '[') & (strArr[0] == ']'):
    answer = answer + 3
    tmpStack.pop()
  elif (tmpStack[-1] == '(') & (strArr[0] == ')'):
    answer = answer + 2
    tmpStack.pop()
  else:
    answer = 0

#
# while(len(strArr)>0):
#   tmpStack.append(strArr.pop(0))
#   if len(tmpStack)>=2:
#
#
#
#
#
#     if (tmpStack[-2] == '[') & (tmpStack[-1] == ']'):
#       tmpStack.pop()
#       tmpStack.pop()
#       if len(tmpStack) > 0:
#         answer = answer * 3
#       else:
#         answer = answer + 3
#     elif (tmpStack[-2] == '(') & (tmpStack[-1] == ')'):
#       tmpStack.pop()
#       tmpStack.pop()
#       if len(tmpStack) > 0:
#         answer = answer * 2
#       else:
#         answer = answer + 2
#
#   else:
#     tmpStack.append(strArr.pop(0))
#     answerArr.append(answer)
#     answer = 0
#
#   print(tmpStack, answer)
# answerArr.append(answer)
#
# if len(tmpStack) > 0:
#   print(0)
# else:
#   print(answerArr)
#


