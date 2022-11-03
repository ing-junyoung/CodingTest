# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120906

# 내 답안

def solution(n):
    
    num_list = list(map(lambda x:int(x) , list(str(n))))
    answer = sum(num_list)
    return answer
  
  # list map은 자주 이용하게 되므로 숙지하기. 
  
  # map의 맨 뒤엔 iterable한 인자 모음이 들어가야 한다. range(0,10) 등.. 
  
  
