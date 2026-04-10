n,m=map(int,input().split())

visitor = list(map(int,input().split()))
result=[]

result.append(sum(visitor[:m]))

for i in range(m,n):
    result.append(result[-1]+visitor[i]-visitor[i-m])

if max(result)==0:
    print("SAD")
else:
    print(max(result))
    print(result.count(max(result)))
    