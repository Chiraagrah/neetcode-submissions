class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        visited = set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    visited.add((x,y))
                    queue.append([x,y])
        level = 0
        while queue:
            length = len(queue)
            for cnt in range(length):
                x,y = queue.popleft()
                grid[x][y] = level
                for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = x+dx,y+dy
                    if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and (nx,ny) not in visited and grid[nx][ny]==2147483647:
                        visited.add((nx,ny))
                        queue.append([nx,ny])
            level += 1
        