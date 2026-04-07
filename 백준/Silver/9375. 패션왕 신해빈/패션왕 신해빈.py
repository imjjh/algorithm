n = int(input())

for i in range(n):
    m = int(input())
    clothes={}
    answer = 1
    for j in range(m):
        name, clothing_type = input().split()
        
        if clothing_type not in clothes:
            clothes[clothing_type]=[]
        
        clothes[clothing_type].append(name)

    for key in clothes:
        answer *= len(clothes[key])+1
    
    answer -= 1
    print(answer)

