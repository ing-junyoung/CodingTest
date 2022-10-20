# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42577




# 모범 답안 

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


  
 
# 내풀이 
def solution(phone_book):
    phone_book.sort()
    answer = True
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]) == True:
            answer = False
            break
    return answer
  
  
  # sort를 통해 정렬하면 리스트 내 현재와 바로 뒤에 있는 원소끼리만 비교하면 되므로 효율성을 매우 높일 수 있음을 깨달았음
  # 또한 중간에 접두사가 포함된 것을 찾으면 break 함으로써, 효율성 확보 
