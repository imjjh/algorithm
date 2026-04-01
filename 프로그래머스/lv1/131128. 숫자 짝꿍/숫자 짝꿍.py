def solution(X, Y):
    count_x=[0]*10
    count_y=[0]*10
    ans = [0]*10
    
    # x 카운트
    for i in range(len(X)):
        curr_num=int(X[i])
        count_x[curr_num]+=1
    # y 카운트
    for i in range(len(Y)):
        curr_num=int(Y[i])
        count_y[curr_num]+=1

    for i in range(10):
        ans[i] = min(count_x[i],count_y[i])
        
    if sum(ans)==0:
        return "-1"
    
    answer = ""
    
    for i in reversed(range(10)):
        if ans[i] == 0:
            continue
        answer += str(i)*ans[i]
    
    if answer[0]=="0":
        answer="0"
    
    return answer
    
    
