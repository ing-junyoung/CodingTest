# 2581 

sosoo = []


# 소수없으면 -1을 print

M = int(input())
N = int(input())
num_list = [i for i in range(M,N+1)]

for i in num_list:
    
    cnt = [1 if i%j==0 else 0 for j in range(1 , i+1)]
    
    if sum(cnt) == 2:
        sosoo.append(i)

    else:
        continue
        
print(sum(sosoo) , min(sosoo) , sep = '\n') if sosoo else print(-1)     

# 아래 것은 탈출문이 있기 때문에 훨씬 효율적임 

M = int(input())
N = int(input())
num_list = [i for i in range(M,N+1)]


sosoo = []

for i in num_list:
    
    
    if i == 1:
        continue
        

    for j in range(2 , i):
        if i%j == 0:
            break
            
    else: 
        sosoo.append(i)
        
print(sum(sosoo) , min(sosoo) , sep = '\n') if sosoo else print(-1)  
