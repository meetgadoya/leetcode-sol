    def numIslands(self, grid):
        if not grid:
            return 0
        a = len(grid)
        b = len(grid[0])
        c = 0  # Count

        global v
        v = [[0] * b for i in range(a)]  # Visited

        i = j = 0
        while (i < a):
            j = 0
            while (j < b):
                if (int(grid[i][j]) == 1 and v[i][j] == 0):
                    self.helper(grid, i, j)
                    # print(v)
                    c = c + 1
                j = j + 1
            i = i + 1

        return c

    def helper(self, grid, i, j):
        global v

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0' or v[i][j]:
            return
        v[i][j] = 1
        self.helper(grid, i + 1, j)
        self.helper(grid, i - 1, j)
        self.helper(grid, i, j - 1)
        self.helper(grid, i, j + 1)

