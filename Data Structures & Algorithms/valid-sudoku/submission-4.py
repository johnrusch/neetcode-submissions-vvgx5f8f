class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        boxes = [[set() for _ in range(len(board) // 3)] for _ in range(len(board) // 3)]

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rows[row] or
                    board[row][col] in cols[col] or
                    board[row][col] in boxes[row // 3][col // 3]):
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                boxes[row // 3][col // 3].add(board[row][col])

        return True