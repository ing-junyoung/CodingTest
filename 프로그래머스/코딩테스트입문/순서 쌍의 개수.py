# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120836

# 내 답안

def solution(n):
    #answer = 0
    answer = []
    for i in range(1,n+1):
        if n%i == 0:
            answer.append((i,n/i))
                
    answer = len(answer)
    return answer
