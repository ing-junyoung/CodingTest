def solution(my_string):
    
    #answer = []
    import re
    answer = re.findall(r'\d' , my_string)
    answer.sort()
    
    answer = [int(i) for i in answer]
    return answer


def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])


