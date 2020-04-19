class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        n_rows = len(grid)
        n_cols = len(grid[0])

        for r in range(n_rows):
            for c in range(n_cols):
                # skip top-left
                if r == c == 0:
                    continue
                # first row
                elif r == 0:
                    grid[r][c] = grid[r][c] + grid[r][c-1]
                # first col
                elif c == 0:
                    grid[r][c] = grid[r][c] + grid[r-1][c]
                else:
                    grid[r][c] = grid[r][c] + min(grid[r][c-1], grid[r-1][c])

        # return bottom-right
        return grid[r][c]