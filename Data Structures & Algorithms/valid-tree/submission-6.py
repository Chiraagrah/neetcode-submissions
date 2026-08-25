class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 != len(edges):
            return False
        dic = defaultdict(list)
        for x,y in edges:
            dic[x].append(y)
            dic[y].append(x)
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbors in dic[node]:
                if neighbors not in visited:
                    dfs(neighbors)
        dfs(0)
        return len(visited) == n