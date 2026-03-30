class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for row in range(len(board)):
            for col in range(len(board[row])):
                square = board[row][col]
                if square == ".":
                    continue
                
                if square in rows[row] or square in cols[col] or square in boxes[row // 3][col // 3]:
                    return False

                rows[row].add(square)
                cols[col].add(square)
                boxes[row // 3][col // 3].add(square)

        return True
