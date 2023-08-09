# 10807

N = int(input())
num = list(map(int , input().split()))
goal = int(input())


cnt = 0
for i in num:
    
    if i == goal:
        cnt += 1
        
print(cnt)
