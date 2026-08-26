class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append((v,t))
        visited = set()
        heap = [(0,k)]
        heapq.heapify(heap)
        dist =[float("inf")]*n
        dist[k-1] = 0
        while heap:
            cur_time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            dist[node-1] = cur_time
            for neighbour, nt in graph[node]:
                heapq.heappush(heap,(cur_time + nt, neighbour))
        return max(dist) if len(visited)==n else -1
            
        
                