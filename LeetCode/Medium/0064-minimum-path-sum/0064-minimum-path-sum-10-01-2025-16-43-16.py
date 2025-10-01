class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0 for i in range(m)] for j in range(n)]
        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1,n):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for y in range(1,m):
            for x in range(1,n):
                dp[x][y] = grid[x][y] + min(dp[x][y-1] , dp[x-1][y])
        # print(dp)
        return dp[n-1][m-1]