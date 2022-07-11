from heapq import heappop, heappush, heapify

def solution(scoville, K):
    heapify(scoville)
    
    for i in range(1000000):
        try:
            heappush(scoville, heappop(scoville) + heappop(scoville) * 2)
        except:
            return -1
        
        if scoville[0] >= K:
            return i + 1