# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42579


# 모범 답안

def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer
  
  
# 내 답안 


def solution(genres, plays):
    #answer = []
    # 일차적으로, dictonary 형태로 만든 뒤 내림차순으로 정렬을 해보기
    # {key : 전체개수 , [(0,n) , (1,m) ... , key2:...]
    answer = []
    table = {}
    
    for i , genre in enumerate(genres):
        # 이미 key가 있으면 추가만
        if genre in table.keys():
            table[genre][0] += plays[i] #전체 개수 누적합
            table[genre][1].append( (i , plays[i]) )
        # 없으면 생성해주기
        else:
            #table[genre][0] = plays[i]
            table[genre] = [plays[i] , [(i , plays[i])]]
            
    table2 = sorted(table.values() , reverse = True)
    # table2 = [3100,(0,3) , (1,5)].. 
    # song[1] = [(0,3) , (1,5) , (2,10) .... ] # 2개만 뽑아내기 
    # sorted(song[1] , key = (lambda x: (-x[1] , x[0]))) :: 고유번호 정렬 완료
    
    for song in table2:
        answer.extend([i[0] for i in sorted(song[1] , key = (lambda x: (-x[1] , x[0])))][:min(2,len(song[1]))])
    

    return answer
  
  
# 자료 구조를 빠르게 정의하고 , sorted 사용할 때 lambda를 사용하면 쉽게 해결 가능 
# for문을 이용해 list를 생성하는 것은 단골이므로 자유자재로 사용가능하도록 
