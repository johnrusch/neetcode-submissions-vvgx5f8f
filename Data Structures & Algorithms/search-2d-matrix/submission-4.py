class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        row = None

        while l <= r:
            mid = (l + r) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                row = matrix[mid]
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1

        if row == None:
            return False

        l, r = 0, len(row) - 1
        while l <= r:
            m = (l + r) // 2
            if target == row[m]:
                return True
            if target < row[m]:
                r = m - 1
            else:
                l = m + 1

        return False