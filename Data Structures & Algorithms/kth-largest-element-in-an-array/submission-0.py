import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num=[-x for x in nums]
        heapq.heapify(num)
        for _ in range(k-1):
            heapq.heappop(num)
        return -heapq.heappop(num)