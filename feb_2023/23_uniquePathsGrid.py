# You are given a matrix grid of n x  m size consisting of values 0 and 
# 1. A value of 1 means that you can enter that cell and 0 implies that entry to that cell is not allowed.
# You start at the upper-left corner of the grid (1, 1) and 
# you have to reach the bottom-right corner (n, m) such that you 
# can only move in the right or down direction from every cell.
# Your task is to calculate the total number of ways of reaching the target modulo (109+7).

def uniquePaths(self, n, m, grid):
        if grid[0][0] == 0 or grid[n-1][m-1] == 0:
            return 0
        if n < m:
            return self.uniquePaths(m, n, list(zip(*grid)))
        dp = [0 for _ in range(m)]
        dp[0] = 1
        mod = 1000000000 + 7
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1]
                    dp[j] %= mod
        return dp[m-1] 
