A , B = map(int , input().split()) # 현재 시간 

C = int(input()) # 요리 소요 시간


total_m = B + C 

A , B  = A + (total_m // 60)  , total_m % 60 

if A > 23:
    
    print(A - 24 , B)
    
else :
    print(A ,B)
