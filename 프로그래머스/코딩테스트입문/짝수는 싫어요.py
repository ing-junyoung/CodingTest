# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120813

# 내 답안

def solution(n):
    answer = []
    
    #answer = [i for i in range(1,n+1) if i%2 != 0] # 한줄 코딩 
    
    # 다른 풀이 
    
    for i in range(1,n+1):
        if i % 2 != 0:
            answer.append(i)
        else:
            continue
    
    return answer
  
  
  
  # if문 / for loop를 이용해 list를 생성하면 한줄 해결 가능 
