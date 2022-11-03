# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120822

# 내 답안

def solution(my_string):
    my_string = list(my_string)
    my_string.reverse()
    answer = "".join(my_string)
    return answer
  
  
  # reverse와 sort안에 reverse는 역할이 다름 
