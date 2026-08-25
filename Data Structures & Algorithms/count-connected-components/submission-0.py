class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dic = defaultdict(list)
        for x,y in edges:
            dic[x].append(y)
            dic[y].append(x)
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbours in dic[node]:
                if neighbours not in visited:
                    dfs(neighbours)
        count = 0
        for x in range(n):
            if x not in visited:
                count+=1
                dfs(x)
        return count