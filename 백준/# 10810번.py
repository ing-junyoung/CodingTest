# 10810

N , M = map(int , input().split())

bucket = [0] * N 

for _ in range(M):
    
    i , j , k = map(int , input().split())
    
    # 한줄 표현 
    # basket[i-1:j] = [k for _ in range(j-i+1)]
    
    for idx in range(i-1,j):
        
        bucket[idx] = k
        
print(*bucket)
