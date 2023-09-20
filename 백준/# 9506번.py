# 9506 



while True:
    
    num_list = []
    
    
    N  = int(input())
    
    
    if N == -1 :
        break

    
    for i in range(1 , N+1):
    
        if N%i == 0 :
            num_list.append(i)

        else:
            continue
            
            
            
    if sum(num_list[:-1]) == num_list[-1]:
        
        
        print(num_list[-1] ,'=' ,
              ' + '.join([str(i) for i in num_list[:-1]]) )
        
    else:
        print('{} is NOT perfect.'.format(num_list[-1]))
