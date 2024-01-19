class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        dp = [row[:] for row in matrix]
        
        for i in range(1, rows):
            for j in range(cols):
                left = dp[i-1][j-1] if j - 1 >= 0 else float('inf')
                mid = dp[i-1][j] 
                right = dp[i-1][j+1] if j + 1 < cols else float('inf')
                
                dp[i][j] += min(left, mid, right)
                
        return min(dp[-1])
        
        