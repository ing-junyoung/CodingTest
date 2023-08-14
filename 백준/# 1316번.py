# 1316

N = int(input())

answer = N 



for _ in range(N):
    
    word = input()
    
    
    i = 0

    while word != '' :
        
        cnt = word.count(word[i])
        check = len(set(word[i : i+cnt]))
        
        if check == 1:
            
            word = word[cnt:]
            
        else:

            answer -= 1 
            
            break
            
