from collections import defaultdict

n = int(input())
tang = list(map(int, input().split()))

count = defaultdict(int)


left = 0
result = 0

for right in range(n):
    count[tang[right]]+=1
    while len(count) > 2:
        count[tang[left]] -= 1
        if count[tang[left]] == 0:
            del count[tang[left]]

        left += 1
    
    result = max(result,right - left + 1)

print(result)