# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120825

# 내 답안

def solution(my_string, n):
    l = list(my_string)
    answer = ''
    for i in l:
        answer += i*n
    return answer
  
  
  # 문자를 list로 바꾸면 각 요소를 원소로하는 len(str)만큼의 길이를 가진 리스트가 생성됨. 
  # 각 요소에 대해 for loop를 하면서 숫자만큼 곱해주어 새로운 리스트의 원소를 생성 
