# 25206
# 과목명이 몇개인지 모를 때.. (20개 고정임을 나중에 발견;)

gpa_dict = {'A+' : 4.5 , 'A0' : 4.0 ,
'B+' : 3.5 , 'B0' : 3.0,
'C+' : 2.5 , 'C0' : 2.0 ,
'D+' : 1.5 , 'D0' : 1.0,
'F' : 0.0}

gpa_sum = 0 
gpa_cnt = 0 

while True:
    
    try:
        sub  , cnt , gpa = map(str , input().split())
        
        if gpa == 'P':
            pass
        
        else:
            gpa_cnt += float(cnt) # 분모
            gpa_sum += float(cnt) * gpa_dict[gpa]  # 분자
            
    except:
        print(gpa_sum / gpa_cnt)
        break
        
