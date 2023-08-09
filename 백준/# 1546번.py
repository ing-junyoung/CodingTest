# 1546

N = int(input())
score = list(map(int , input().split()))

new_score = [i/max(score)*100 for i in score]

print(sum(new_score) / N)
