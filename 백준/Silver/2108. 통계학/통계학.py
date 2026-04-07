from collections import Counter
import sys

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))


arr.sort()

cnt = Counter(arr)

if 0 <= int((sum(arr)/len(arr))):
    print(int((sum(arr)/len(arr))+0.5))
else:
    print(int((sum(arr)/len(arr))-0.5))
    
print(arr[len(arr)//2])



max_freq = max(cnt.values())
candidates = []
for key,value in cnt.items():
    if value == max_freq:
        candidates.append(key)
    
candidates.sort()
if len(candidates)==1:
    print(candidates[0])
else:
    print(candidates[1])

print(max(arr)-min(arr))