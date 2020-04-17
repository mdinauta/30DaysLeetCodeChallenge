class Solution(object):
    def dfs(self, i, j, grid, visited):
        visited[i][j] = True
        neighbors = [(i, j-1), 
                     (i-1, j), 
                     (i, j+1), 
                     (i+1, j)]

        for neighbor in neighbors:
            row_neighbor = neighbor[0]
            col_neighbor = neighbor[1]
            if row_neighbor >= 0 and col_neighbor >= 0:
                # if neighbor exists
                if (row_neighbor < len(visited)) & (col_neighbor < len(visited[0])):
                    if not visited[row_neighbor][col_neighbor]:
                        if grid[row_neighbor][col_neighbor] == "1":
                            self.dfs(row_neighbor, col_neighbor, grid, visited)

        return visited

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        n_rows = len(grid)
        n_cols = len(grid[0])
        n_islands = 0
        visited = [[False for j in range(n_cols)]for i in range(n_rows)] 

        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == '1':
                    if visited[i][j] == False:
                        n_islands += 1
                        visited = self.dfs(i, j, grid, visited)

        return n_islands
