def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1,arr2):
        row = format(a | b,'b').zfill(n)
        answer.append(row.replace('1','#').replace('0',' '))
    return answer