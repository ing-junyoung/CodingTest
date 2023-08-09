# 10811

N , M = map(int , input().split())

num_list = [i for i in range(1,N+1)]


for _ in range(M):
    
    i , j = map(int , input().split())
    
    temp = num_list[i-1:j]
    
    temp.reverse()
    
    num_list[i-1:j] = temp
    
print(*num_list)
    
