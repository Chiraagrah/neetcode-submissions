from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        visited = [False] * n
        total_cost = 0
        
        for _ in range(n):
            # 1. Pick the unvisited node with the smallest distance to the MST
            curr = -1
            curr_dist = float('inf')
            for i in range(n):
                if not visited[i] and min_dist[i] < curr_dist:
                    curr_dist = min_dist[i]
                    curr = i
            
            # 2. Add node to MST
            visited[curr] = True
            total_cost += curr_dist
            
            # 3. Update min distance to remaining unvisited neighbors
            x1, y1 = points[curr]
            for next_node in range(n):
                if not visited[next_node]:
                    x2, y2 = points[next_node]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    if dist < min_dist[next_node]:
                        min_dist[next_node] = dist
                        
        return total_cost