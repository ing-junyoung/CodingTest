def solution(numbers):
    answer = 0
    
    numbers = sorted(numbers)
    
    answer  = max(numbers[0]*numbers[1] , numbers[-1] * numbers[-2])
    
    return answer


def solution(numbers):
    numbers = sorted(numbers)
    return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2]) 



def solution(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])
