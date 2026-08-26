

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append((v,t))
        dist = defaultdict(int)
        queue = deque([k])
        dist[k] = 0
        while queue:
            cur_node = queue.popleft()
            cur_dist = dist[cur_node]
            for neighbour,nt in graph[cur_node]:
                if neighbour not in dist or cur_dist+nt < dist[neighbour]:
                    dist[neighbour] = cur_dist + nt  
                    queue.append(neighbour)
        return -1 if len(dist)!=n else max(dist.values())
            
                