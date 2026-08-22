class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            head = root
            for char in word:
                if char not in head.children:
                    head.children[char] = TrieNode()
                head = head.children[char]
            head.word = word
        
        result = []

        def dfs(x,y,parent):
            char = board[x][y]
            child = parent.children[char]
            if child.word:
                result.append(child.word)
                child.word = None
            
            board[x][y] = '#'
            
            for dir_x, dir_y in ((1,0),(0,1),(-1,0),(0,-1)):
                
                nx = x+dir_x
                ny = y+dir_y
                
                if 0<=nx<len(board) and 0<=ny<len(board[0]) and board[nx][ny] in child.children:
                    dfs(nx,ny,child)
            
            board[x][y] = char

            if not child.children:
                del parent.children[char]

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] in root.children:
                    dfs(x,y,root)
    
        return result
            
                




