# 10813


#[*range(i,j)]  ==> range 범위 요소 list 생성 


N , M = map(int , input().split())

list_N = [i for i in range(1,N+1)]

for _ in range(M):
    
    a , b = map(int , input().split())
    
    list_N[a-1] , list_N[b-1] = list_N[b-1] , list_N[a-1]
    
print(*list_N)
