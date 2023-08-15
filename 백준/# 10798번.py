# 10798 


# try except? 


matrix = [list(map(str , input())) for _ in range(5)]

max_len = 0 

for i in matrix:
    
    if len(i) >= max_len:
        max_len = len(i)


word = ''



for i in range(max_len):
    
    temp = ''

    for j in range(5):

        try:
            word += matrix[j][i]
        
        except:

            continue
            
            
print(word)      
