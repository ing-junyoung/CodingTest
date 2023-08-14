# import sys 
# word = sys.stdin.readline()

# 1157

word = input().upper()


word_basket = list(word)


cnt = []

for i in list(set(word_basket)):
    
    cnt.append(word_basket.count(i))


key = []
for i in range(len(cnt)):
    if cnt[i] == max(cnt):
        key.append(list(set(word))[i])
        

print('?') if len(key) > 1 else print(*key)
