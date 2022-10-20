# 문제 링크 :  https://school.programmers.co.kr/learn/courses/30/lessons/42576


# collections 함수 사용해서 dictionary 차이를 구할 수 있음을 알게 됨
# 이 외에도, 문자에 hash함수 사용해서 푸는 것도 확인 

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
