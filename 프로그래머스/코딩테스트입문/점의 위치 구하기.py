# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120841

# 내 답안

def solution(dot):
    #answer = 0
    
    if dot[0]>0 and dot[1]>0:
        answer = 1
    elif dot[0]<0 and dot[1]>0:
        answer = 2
    elif dot[0]<0 and dot[1]<0:
        answer = 3
    else:
        answer = 4
    return answer
