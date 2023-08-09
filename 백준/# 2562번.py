# 2562 

# 굳이 이렇게 풀 필요 없을듯 


max_n = int(input())
i = 1
cnt = 1


while True:
    
    try:
        cnt += 1
        n = int(input())
        if n > max_n:
            max_n = n 
            i = cnt
        else:
            pass
        
        
    except:
        break
        
print(max_n)
print(i)
