# 1085

x , y , w , h = map(int , input().split())

print(min(x , y , w-x , h-y))


def solution(N):
    prime_factors = []
    i = 2
    while i * i <= N:
        while N % i == 0:
            N //= i
            prime_factors.append(i)
        i += 1
    if N > 1:
        prime_factors.append(N)
    return prime_factors
    
    
if __name__ == '__main__':
    # 1 일 때 주의
    from sys import stdin, stdout
    N = int(stdin.readline().rstrip())
    answer = solution(N)
    stdout.write('\n'.join(map(str, answer)) + '\n')
