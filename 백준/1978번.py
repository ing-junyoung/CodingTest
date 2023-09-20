# 1978 


N = int(input())

num_list = list(map(int , input().split()))

sosoo_cnt = 0
    
for i in num_list:

    cnt = [1 if i%j==0 else 0 for j in range(1 , i+1)]

    if sum(cnt) == 2:
        sosoo_cnt +=1

    else:
        continue

print(sosoo_cnt)




# other ver.

import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
count = 0
for i in num_list:
    if i == 1:
        continue
    for j in range(2, i):
        if i%j == 0:
            break
    else:    
        count += 1
print(count)
