# 2720 

coin = [25 , 10 , 5 , 1]

N = int(input())

for i in range(N):
    
    pay = int(input())
    
    cnt = []
    
    for j in coin:
        
        num = pay // j # j의 개수 
        
        pay = pay - num * j
        
        cnt.append(num)
        
    print(*cnt)
