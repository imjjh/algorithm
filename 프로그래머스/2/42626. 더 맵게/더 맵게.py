import heapq

def solution(scoville, K):
    heap = scoville
    count = 0
    heapq.heapify(heap)

    while heap[0] < K:
        
        if len(heap) <2:
            return -1
        min_val = heapq.heappop(heap)
        min_val2 = heapq.heappop(heap)
        
        heapq.heappush(heap, min_val + (min_val2 * 2))
        count+=1
        
    
    return count