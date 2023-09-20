# 1193 

# 짝수일 때 , 홀수일 때 구분. 분모가 커지고 분자가 작아지는
# 상호 반대 방향 감소 증가


N = int(input())


i = 1

while True:
    
    if N-i > 0:
        
        N = N-i
        
        i += 1 
        
    else:
        
        if (i-1)%2 == 0:   # 짝수번째까지 지워졌다면 홀수규칙
            
            i +=1
            
            print('{}/{}'.format(i-N , N))
            break
            
        else:  # 홀수번째까지 지워졌다면 짝수규칙
            
            i += 1
            
            print('{}/{}'.format(N , i-N))
            break
