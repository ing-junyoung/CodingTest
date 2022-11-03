# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120818

# 내 답안 

def solution(price):
    if price >= 500000:
        answer = price*0.8
    elif price >= 300000:
        answer = price*0.9
    elif price >= 100000:
        answer = price *0.95
    else:
        answer = price
        
    #answer = 0
    return int(answer)
  
  
  # 그냥 간단한 if문 쓰면 됨 
