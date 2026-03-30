class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sqs = [[set() for _ in range(3)] for _ in range(3)]

        for row in range(len(board)):
            for col in range(len(board[row])):
                num = board[row][col]
                if num in rows[row] or num in cols[col] or num in sqs[row // 3][col // 3]:
                    return False
                if num != '.': 
                    rows[row].add(num)
                    cols[col].add(num)
                    sqs[row // 3][col // 3].add(num)

        return True
