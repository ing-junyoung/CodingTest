# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42578



# 모범 답안 


def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer


# 내 답안

import collections 


def solution(clothes):
    
    lt = [clothes[i][1] for i in range(len(clothes))]
    lt2 = list(collections.Counter(lt).values())
    temp = 1
    for j in range(len(lt2)):
        temp *= lt2[j] + 1
    answer = temp - 1
    
    return answer
    
    
 # lambda 사용에 익숙해지자. 
 # 종류 별 (key) 개수+1 을 모두 곱한 후 -1을 해주는 아이디어를 떠올리는 게 본 문제의 핵심 point 
