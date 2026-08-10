from typing import List
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [
            (x * x + y * y, x, y)
            for x, y in points
        ]

        heapq.heapify(distances)

        result = []

        for _ in range(k):
            _, x, y = heapq.heappop(distances)
            result.append([x, y])

        return result