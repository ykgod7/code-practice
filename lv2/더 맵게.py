import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0

    while True:
        try:
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
            count += 1
        except:
            return -1
        if scoville[0] >= K:
            break
    return count