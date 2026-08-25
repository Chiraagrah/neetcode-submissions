class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        banana = 0
        queue = deque()
        visited = set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]== 1:
                    banana += 1
                if grid[x][y] == 2:
                    queue.append((x,y))
                    visited.add((x,y))
        if banana == 0 :
            return 0
        if not queue:
            return -1
        minute = -1
        while queue:
            cur_rotten = len(queue)
            for _ in range(cur_rotten):
                rotten_x, rotten_y  = queue.popleft()
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = rotten_x + dx, rotten_y + dy
                    if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] == 1 and (nx,ny) not in visited:
                        banana -= 1
                        queue.append((nx,ny))
                        visited.add((nx,ny))
            minute += 1
        return minute if banana == 0 else -1
            
