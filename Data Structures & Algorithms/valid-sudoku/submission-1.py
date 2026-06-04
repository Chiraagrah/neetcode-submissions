class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(9)]
        column=[set() for _ in range(9)]
        box=[set() for _ in range(9)]

        for x in range(9):
            for y in range(9):
                n = board[x][y]
                if n=='.':
                    continue
                if (n in row[x]) or (n in column[y]) or (n in box[3*(x//3)+(y//3)]):
                    return False
                else:
                    row[x].add(n)
                    column[y].add(n)
                    box[3*(x//3)+(y//3)].add(n)
        return True