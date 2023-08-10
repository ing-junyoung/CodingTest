# 2908 

A , B = map(str , input().split())

new_A , new_B = int(A[::-1]) , int(B[::-1])

print(max(new_A , new_B))
