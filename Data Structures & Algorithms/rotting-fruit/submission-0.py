class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        queue = collections.deque()
            
        for i, row in enumerate(grid):
            for j, spot in enumerate(row):
                if spot == 2:
                    queue.append((i, j, 0))

        while queue:
            r, c, time = queue.popleft()
            res = max(res, time)
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, time + 1))


        for row in grid:
            for spot in row:
                if spot == 1:
                    res = -1

        return res