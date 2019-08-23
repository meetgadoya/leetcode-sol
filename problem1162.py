class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for i in range(n)] for j in range(m)]

        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited[i][j] = 1
                    queue.append((i, j))

        if len(queue) == 0 or len(queue) == m * n:
            return -1
        # direct = [(0,1),(1,0),(0,-1),(-1,0)]
        ans = 0
        while queue:
            i, j = queue.pop(0)
            ans = max(ans, grid[i][j] - 1)

            if i + 1 < m and visited[i + 1][j] == 0:
                queue.append((i + 1, j))
                grid[i + 1][j] = grid[i][j] + 1
                visited[i + 1][j] = 1
            if 0 <= i - 1 and visited[i - 1][j] == 0:
                queue.append((i - 1, j))
                grid[i - 1][j] = grid[i][j] + 1
                visited[i - 1][j] = 1
            if j + 1 < n and visited[i][j + 1] == 0:
                queue.append((i, j + 1))
                grid[i][j + 1] = grid[i][j] + 1
                visited[i][j + 1] = 1
            if 0 <= j - 1 and visited[i][j - 1] == 0:
                queue.append((i, j - 1))
                grid[i][j - 1] = grid[i][j] + 1
                visited[i][j - 1] = 1
        return ans