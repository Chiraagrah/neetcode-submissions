class DSU:
    def __init__(self, size: int):
        self.parent = list(range(size))

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        total_cells = n * n
        
        # O(N^2) position lookup table: pos[val] = (r, c)
        pos = [None] * total_cells
        for r in range(n):
            for c in range(n):
                pos[grid[r][c]] = (r, c)

        dsu = DSU(total_cells)
        unlocked = [[False] * n for _ in range(n)]
        
        start_idx = 0
        end_idx = total_cells - 1

        for t in range(total_cells):
            r, c = pos[t]
            unlocked[r][c] = True
            curr_idx = r * n + c

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and unlocked[nr][nc]:
                    dsu.union(curr_idx, nr * n + nc)

            if unlocked[0][0] and unlocked[n - 1][n - 1] and dsu.find(start_idx) == dsu.find(end_idx):
                return t

        return total_cells - 1