# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/1845


# 모범 답안 
def solution(nums):
    return min(len(nums)/2 , len(set(nums)) )
    
    
  
# 내 풀이

def solution(nums):
    max_length = int(len(nums) / 2)
    temp_max_length = len(list(dict.fromkeys(nums)))

    if max_length <= temp_max_length:
        answer = max_length
    elif max_length > temp_max_length:
        answer = temp_max_length

    return answer
    
    
    
 # set (집합 관련 함수)을 이용하면 간단하게 해결 가능
