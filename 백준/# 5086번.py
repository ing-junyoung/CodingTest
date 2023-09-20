# 5086

while True:
    
    A , B = map(int , input().split())
    
    
    if A+B == 0:
        break
    
    elif B%A == 0:
        print('factor')
    
    elif A%B == 0:
        print('multiple')    
    
    elif (B%A != 0 & A%B == 0):
        print('neither')  
