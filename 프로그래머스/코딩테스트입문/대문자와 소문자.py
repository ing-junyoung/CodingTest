def solution(my_string):
    answer = ''
    
    #my_string +='1'
    for char in my_string:

        if char.isupper():
            answer += char.lower()
        elif char.islower():
            answer += char.upper()
        elif (char.isupper() == False) and (char.islower() == False):
            answer += char
            
    return answer



def solution(my_string):
    answer = ''

    for i in my_string:
        if i.isupper():
            answer+=i.lower()
        else:
            answer+=i.upper()
    return answer
