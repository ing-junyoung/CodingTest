# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12906




# 모범 답안 

def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
  
  
  
  
# 내 답안

def solution(arr):
    answer = []
    answer.append(arr[0])
    arr.pop(0)


    for i in range(len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
                            
    return answer
  
  
  
  # 긴 시간 동안 고민하다가 해결하였음. 
  # pop에 너무 집중한 나머지 쉽게 풀 수 있는 문제에 너무 긴 시간을 투자했음
  # 결국 첫번째 요소를 answer에 append하고 answer의 마지막 요소와 입력값의 인덱싱을 이용해 조건문을 사용함 
  # 모범 답안도 인덱스 슬라이싱을 했는데, 빈 리스트의 [-1:]을 했을 때 오류가 안나고 빈 리스트를 반환한다는 것을 알게 되었음.
  # 나는 list[-1]을 하면 오류가 나길래 안되는 줄 알았기에 , 새로운 방법을 배울 수 있었음. 
  
