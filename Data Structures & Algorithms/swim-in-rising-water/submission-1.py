class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0],0,0)]
        heapq.heapify(heap)
        visited = {(0,0)}
        while heap:
            maxelev,x,y = heapq.heappop(heap)
            if x==len(grid)-1 and y== len(grid[0])-1:
                return maxelev
            for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx,ny  = x+dx, y+dy
                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and (nx,ny) not in visited:
                    heapq.heappush(heap,(max(maxelev,grid[nx][ny]),nx,ny,))
                    visited.add((nx,ny))

