import heapq

def check(wait):
    
    res = []
    heap = wait[:]
    heapq.heapify(heap)
    max_wait = max(wait)
    t = 0
    i = 0 
    while i <= len(wait) and heap:
        
        if t+1 == wait[0]:
            heapq.heappop(heap)
            i += 1
        res.append(len(heap))
        
        t+=1
        while heap and t+1 > heap[0]:
            heapq.heappop(heap)
    
    while t <= max_wait:
        res.append(0)
        t+=1
        
    return res
    


# Example usage
wait = [2, 2, 3, 1]
print(check(wait))








