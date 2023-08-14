# 3003 

white_piece = list(map(int , input().split()))
black_piece = [1 , 1 , 2 , 2 , 2 , 8] # 원래 있어야 할 조각 
temp = []

for i in range(len(black_piece)):
    
    temp.append(black_piece[i] - white_piece[i])
    
print(*temp)
