class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(x,y,index,visited):
            if index == len(word):
                return True
            for dir_x,dir_y in [[0,1],[1,0],[0,-1],[-1,0]]:
                new_dirx = x + dir_x
                new_diry = y + dir_y
                if 0<=new_dirx<len(board) and 0<=new_diry<len(board[0]) and (new_dirx,new_diry) not in visited and board[new_dirx][new_diry] == word[index]:
                    visited.add((new_dirx,new_diry))
                    if backtrack(new_dirx,new_diry,index+1,visited):
                        return True
                    visited.remove((new_dirx,new_diry))
            return False
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y]!=word[0]:
                    continue
                else:
                    if backtrack(x,y,1,{(x,y)}):
                        return True
        return False