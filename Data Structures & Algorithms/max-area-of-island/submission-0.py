class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x,y,count):
            grid[x][y] = 0
            for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = x+dx, y+dy
                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]==1:
                    count = dfs(nx,ny,count+1)
            return count

        res = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                temp = 0
                if grid[x][y]==1:
                    temp = dfs(x,y,1)
                if temp>res:
                    res = temp
        return res