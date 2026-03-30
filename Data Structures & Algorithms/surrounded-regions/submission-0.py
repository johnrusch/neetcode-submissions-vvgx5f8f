class Solution:
    def solve(self, board: List[List[str]]) -> None:
        safe = set()

        def mark_safe(r, c) -> None:
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or (r, c) in safe or board[r][c] != "O":
                return
            
            safe.add((r, c))
            mark_safe(r - 1, c)
            mark_safe(r + 1, c)
            mark_safe(r, c - 1)
            mark_safe(r, c + 1)

        for i in range(len(board[0])):
            if board[0][i] == "O":
                mark_safe(0, i)

            if board[-1][i] == "O":
                mark_safe(len(board) - 1, i)

        for i in range(len(board)):
            if board[i][0] == "O":
                mark_safe(i, 0)

            if board[i][len(board[i]) - 1] == "O":
                mark_safe(i, len(board[i]) - 1)

        # mark other Os with Xs
        for i, row in enumerate(board):
            for j, spot in enumerate(row):
                if spot == "O" and (i, j) not in safe:
                    board[i][j] = "X"