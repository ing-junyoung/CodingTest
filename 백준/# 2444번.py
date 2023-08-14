# 2444

N = int(input())

temp = []

for i in range(1 , N+1):
    temp.append((N-i) * ' ' + (i*2-1) * '*')

for i in reversed(range(1 , N)):
    temp.append((N-i) * ' ' + (i*2-1) * '*')
    
print(*temp , sep = '\n')
