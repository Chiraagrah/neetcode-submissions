class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)]for _ in range(n)]
        blockedrow = set()
        blockeddiag1 = set()
        blockeddiag2 = set()
        result = []
        def backtrack(number,board):
            if number == n:
                result.append(["".join(r) for r in board])
                return
            for x in range(n):
                if board[number][x] == '.' and x not in blockedrow and number+x not in blockeddiag1 and number - x not in blockeddiag2:
                    board[number][x] = 'Q'
                    blockedrow.add(x)
                    blockeddiag1.add(number+x)
                    blockeddiag2.add(number-x)
                    backtrack(number+1,board)
                    board[number][x] = '.'
                    blockedrow.remove(x)
                    blockeddiag1.remove(number+x)
                    blockeddiag2.remove(number-x)
        backtrack(0,board)
        return result

                    
                    
