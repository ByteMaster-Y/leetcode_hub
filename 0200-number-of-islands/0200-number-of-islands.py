class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            # 범위를 벗어나거나 현재 위치가 땅이 아니면 종료
            if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] == '0':
                return 
            
            # 현재 위치를 방문한것으로 표시
            grid[row][col] = '0'
            
            # 상하 좌우에 대한 DFS 실행
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            
        if not grid:
            return
        
        m, n = len(grid), len(grid[0])
        island_count = 0
        
        for i in range(m):
            for j in range(n):
                # '1'을 발견하면 섬이므로 DFS 수행하고 섬 개수를 증가
                if grid[i][j] == '1':
                    island_count += 1
                    dfs(i, j)
                    
        return island_count
            
            