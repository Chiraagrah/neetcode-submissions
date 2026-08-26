class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append([v,t])
        pq = [(0, k)]
        distances = {}
        
        while pq:
            cur_time, cur_node = heapq.heappop(pq)

            if cur_node in distances:
                continue
            
            distances[cur_node] = cur_time
            
            for neighbor, weight in graph[cur_node]:
                if neighbor not in distances:
                    heapq.heappush(pq, (cur_time + weight, neighbor))
        
        return max(distances.values()) if len(distances) == n else -1
            