class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)
            weight = abs(stone1-stone2)
            if weight>0:
                heapq.heappush(heap,-weight)
        return -heap[0] if heap else 0