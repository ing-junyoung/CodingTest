# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120849

# 내 답안 
import re
def solution(my_string):
    answer = ''
    
    answer = re.sub(r"a|e|i|o|u" , '' , my_string)
    
    

    
    return answer 
  
  
  
  # re package내 sub 함수 사용 
  # re.sub("찾을 것" , '이걸로 대체' , 대상 문자)
