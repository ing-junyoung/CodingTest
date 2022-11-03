# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120837

# 내 답안 

def solution(hp):
    # 장군 공격력 : 5
    # 병정 공격력 : 3
    # 일개미 공격력: 1 
    
    answer = 0
    ant = [5,3,1]
    
    for i in ant:
        
        answer += divmod(hp,i)[0]
        
        hp = divmod(hp,i)[1]
    #answer = 0
    return answer
  
  
  # 몫과 나머지를 출력하는 divmod 함수로 쉽게 해결 가능 
