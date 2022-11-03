# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120851

# 내 답안

import re

def solution(my_string):
    
    answer = 0
    
    numbers = re.findall(r'\d' , my_string)
    answer = sum([int(i) for i in numbers])
    
    return answer
  
  
  # re package 내 findall 함수 이용. 
  # findall 함수에서 \d 인자는 숫자를 찾을 때 사용함 d+1,, d+2,,, 1개 초과 2개 초과인 숫자 찾는 것 , 예를 들어 d =7 , d+1 =77 , d+2 =777 .. 
  
  
