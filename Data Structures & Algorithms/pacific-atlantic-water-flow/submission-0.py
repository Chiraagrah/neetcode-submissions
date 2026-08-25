class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        queuePacific = deque()
        queueAtlantic = deque()
        res = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if row == 0 or col == 0:
                    pacific.add((row,col))
                    queuePacific.append((row,col))
                if row == len(heights)-1 or col == len(heights[0])-1:
                    atlantic.add((row,col))
                    queueAtlantic.append((row,col))
        while queuePacific:
            currCellx,currCelly = queuePacific.popleft()
            for dx, dy  in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = currCellx + dx, currCelly + dy
                if 0<=nx<len(heights) and 0<=ny<len(heights[0]) and (nx,ny) not in pacific and heights[nx][ny]>=heights[currCellx][currCelly]:
                    pacific.add((nx,ny))
                    queuePacific.append((nx,ny))
        while queueAtlantic:
            currCellx, currCelly = queueAtlantic.popleft()
            if (currCellx,currCelly) in pacific:
                res.append([currCellx,currCelly])
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx,ny = currCellx + dx, currCelly + dy
                if 0<=nx<len(heights) and 0<=ny<len(heights[0]) and (nx,ny) not in atlantic and heights[nx][ny]>=heights[currCellx][currCelly]:
                    atlantic.add((nx,ny))
                    queueAtlantic.append((nx,ny))
        return res
