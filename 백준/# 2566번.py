# 2566번 

matrix = [list(map(int , input().split())) for _ in range(9)]

max_value = 0 
max_pos = [0 , 0]

for i in range(9):
    
    for j in range(9):
        
        if matrix[i][j] >= max_value: # 모두 0일수도 있기에 등호를 넣어주기
            
            max_value = matrix[i][j]
            max_pos = [i+1 , j+1]
        
        else:
            pass
        
print(max_value)
print(*max_pos)
