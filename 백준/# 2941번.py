# 2941


word = input()

alphabet = [ 'c=' , 'c-' , 'dz=' , 'd-' , 
           'lj' , 'nj' , 's=' , 'z=']


cnt = 0

for i in alphabet:
    
   # print(i , word.find(i))
    if word.count(i) > 0:
        
        cnt += word.count(i)
        word = word.replace(i , ' ')
        
print(cnt + len(word.replace(" " , '')))


# in , * replace 방법으로 코드 효율성을 높이자
