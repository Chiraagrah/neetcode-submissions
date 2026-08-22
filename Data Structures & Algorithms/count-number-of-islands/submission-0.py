class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def dfs(x,y):
            grid[x][y] = '0'
            for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx = x+dx
                ny = y+dy
                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]=='1':
                    dfs(nx,ny)
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]=='1':
                    count += 1
                    dfs(x,y)
        return count 