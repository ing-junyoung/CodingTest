# 2675
T = int(input())

for _ in range(T):
    
    R , word = map(str , input().split())
    
    R = int(R)
    
    cnt = ''
    
    for i in word:
        
        cnt += R * i
    
    print(cnt)
