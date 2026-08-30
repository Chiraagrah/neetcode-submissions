class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if n == 1:
            return 0

        parent = list(range(n*n))

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i,j):
            rootI = find(i)
            rootJ = find(j)
            if rootI!=rootJ:
                parent[rootJ] = rootI

        vals = [None]*(n*n)

        for x in range(n):
            for y in range(n):
                vals[grid[x][y]] = (x,y)

        visited = [False] * (n * n)
        start_val = grid[0][0]
        end_val = grid[n - 1][n - 1]

        for t in range(n*n):
            x,y  = vals[t]
            idx = x*n + y
            visited[idx] = True
            for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx,ny = x+dx, y+dy
                n_idx = nx*n + ny
                if 0<=nx<n and 0<=ny<n and visited[n_idx]:
                    union(grid[x][y],grid[nx][ny])
            if visited[0] and visited[n*n -1] and find(start_val) == find(end_val):
                return t
        return (n*n) - 1

