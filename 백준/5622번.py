# 5622

number = input()

dial = ['ABC' , 'DEF' , 'GHI' , 'JKL' , 
       'MNO' , 'PQRS' , 'TUV' , 'WXYZ']

time = 0 

for i in number:
    
    for idx , dial_element in enumerate(dial):
        
        if i in dial_element:
            
            time += idx + 3
            
            break
        
        else:
            pass
print(time)     
