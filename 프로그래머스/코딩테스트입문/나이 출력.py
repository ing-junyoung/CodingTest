# Q. 머쓱이는 40살인 선생님이 몇 년도에 태어났는지 궁금해졌습니다. 나이 age가 주어질 때, 2022년을 기준 출생 연도를 return 하는 solution 함수를 완성해주세요.


def solution(age):
    if 0<age<=120:  
        birth = 2022 - age + 1
    # 임의로 예외 사항도 출력 만들어 봄 
    else: 
        birth = 'error!'
    return birth
