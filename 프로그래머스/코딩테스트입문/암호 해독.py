def solution(cipher, code):
    answer = ''
    
    answer = list(map(lambda x:list(cipher)[x] , range(code-1,len(cipher),code)))
    
    answer = ''.join(answer)
    return answer



def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer
