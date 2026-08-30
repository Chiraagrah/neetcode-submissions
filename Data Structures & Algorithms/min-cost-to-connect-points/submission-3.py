class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = list(range(n))
        def find(i:int) -> int:
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        edges = []
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                edges.append((dist,i,j))
        heapq.heapify(edges)
        cost = 0
        edges_used = 0
        while edges and edges_used< n-1:
            cur_cost, u, v = heapq.heappop(edges)
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                parent[root_v] = root_u
                cost+= cur_cost
                edges_used +=1
        return cost


