def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        command = commands[i]
        arr = array[command[0] - 1 : command[1] - 1 + 1] # 1 based -> 0 based
        arr.sort()
        answer.append( arr[command[2]-1] ) # 1 based -> 0 based
    
    return answer
        