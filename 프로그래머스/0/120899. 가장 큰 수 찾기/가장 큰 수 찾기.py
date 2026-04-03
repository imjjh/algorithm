def solution(array):
    max_array=max(array)
    answer = [max_array,array.index(max_array)]
    return answer