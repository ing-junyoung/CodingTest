# 11653 

N = int(input())
i = 4 

while N > 1:
    
    if N % 2 == 0:
        N = N/2
        print(2)
    elif N % 3 == 0:
        N = N/3
        print(3)
        
        
    else: 
  
        while N >= i:
            
            if N % i == 0:
                N = N/i
                print(i)
                
            else:
                i +=1
