A , B , C = map(int , input().split())


if A==B==C:
    print(10000 + A*1000)
    
elif (A!=B!=C) and (A!=C!=B): # 다 다름
    print(max(A,B,C) * 100)
    
else:
    print(1000 + sorted([A,B,C])[1] * 100)
