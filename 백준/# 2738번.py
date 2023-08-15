# 2738번

N , M = map(int , input().split())

matrix_A = [list(map(int , input().split())) for _ in range(N)]
matrix_B = [list(map(int , input().split())) for _ in range(N)]
matrix_sum = [[0 for _ in range(M)] for _ in range(N)]


for i in range(N):
    
    for j in range(M):
        
        matrix_sum[i][j] = matrix_A[i][j] + matrix_B[i][j]
        
for k in matrix_sum:
    print(*k)
