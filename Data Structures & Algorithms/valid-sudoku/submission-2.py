class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Array of 9 integers, all initialized to 0 (binary: 000000000)
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                # Create a bitmask by shifting 1 left by the digit's value
                # e.g., if val is '5', pos = 1 << 5 (binary: 000100000)
                pos = 1 << int(val)
                box_idx = (r // 3) * 3 + (c // 3)

                # Bitwise AND (&): Check if this bit is already flipped to 1
                if (rows[r] & pos) or (cols[c] & pos) or (boxes[box_idx] & pos):
                    return False

                # Bitwise OR (|=): Flip the bit to 1 to mark it as seen
                rows[r] |= pos
                cols[c] |= pos
                boxes[box_idx] |= pos

        return True