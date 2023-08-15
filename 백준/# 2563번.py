# 2563

N = int(input())

paper = [[0 for _ in range(100)] for _ in range(100)]


for _ in range(N):
    
    x , y = map(int , input().split())
    
    for i in range(y , y+10):
        
        paper[i-1][x-1 : x+9] = [1] * 10 
            
        

cnt = 0 

for i in paper:
    cnt += i.count(0)
    
print(100*100 - cnt)
