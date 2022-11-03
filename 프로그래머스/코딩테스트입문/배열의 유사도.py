# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120903

# 내 답안

def solution(s1, s2):
    
    # 교집합 이용 
    if list(set(s1) & set(s2)) != []:
        answer = len(list(set(s1) & set(s2)))
    else:
        answer = 0 
        
        
    return answer
  
  
  # 오랜만에 등장한 set 함수를 이용하는 문제 
  # 교집합을 구하면 된다. (set은 기본적으로 unique가 적용됨)
