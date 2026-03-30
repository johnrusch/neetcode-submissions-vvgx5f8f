# create arrays for rows, cols, and boxes, each full of 9 sets
# iterate through the board, probably by row
#   for each spot, verify that the spot's value hasn't been seen in
#   the same row, col, and box

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(len(board)):
            row = i
            for j in range(len(board[row])):
                col = j
                spot = board[i][j]
                if spot == '.':
                    continue
                if spot in rows[row] or spot in cols[col] or spot in boxes[row // 3][col // 3]:
                    return False

                rows[row].add(spot)
                cols[col].add(spot)
                boxes[row // 3][col // 3].add(spot)

        return True
