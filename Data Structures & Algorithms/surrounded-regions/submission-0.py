class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue = deque()
        visited = set()
        Os = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row == 0 or col == 0 or row == len(board)-1 or col == len(board[0])-1) and board[row][col] == 'O':
                    visited.add((row,col))
                    queue.append((row,col))
                elif board[row][col]== 'O':
                    Os.add((row,col))
        while queue:
            currow, currcol = queue.popleft()
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = currow + dx, currcol + dy
                if 0<=nx<len(board) and 0<=ny<len(board[0]) and (nx,ny) not in visited and board[nx][ny]=='O':
                    visited.add((nx,ny))
                    queue.append((nx,ny))
                    Os.remove((nx,ny))
        for row,col in Os:
            board[row][col] = 'X'
        
