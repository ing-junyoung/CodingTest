
def solution(rsp):
    answer = ''
    
    for temp in rsp:
        if temp =='2':
            answer += '0'
        elif temp =='0':
            answer +='5'
        elif temp == '5':
            answer +='2'
            
    return answer



def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)
