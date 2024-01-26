class Solution:
    def findPaths(self, m: int, n: int, N: int, x: int, y: int) -> int:
        # 모듈로 연산에 사용
        M = 10**9 + 7
        
        # dp 배열 초기화
        dp = [[0] * n for _ in range(m)]
        dp[x][y] = 1
        
        # 결과를 저장할 변수 초기화
        count = 0
        
        # 공을 최대 N번 이동할 때까지 반복
        for moves in range(1, N + 1):
            # 현재 이동 횟수에서의 임시 배열 초기화
            temp = [[0] * n for _ in range(m)]
            
            # 격자의 각 셀에 대해 이전 이동 횟수의 값들을 참조하여 업데이트
            for i in range(m):
                for j in range(n):
                    # 공이 격자에 닿을 때 마다 업데이트
                    if i == m - 1 :
                        count = (count + dp[i][j]) % M
                    if j == n - 1:
                        count = (count + dp[i][j]) % M
                    if i == 0:
                        count = (count + dp[i][j]) % M
                    if j == 0:
                        count = (count + dp[i][j]) % M
                        
                     # 현재 셀의 값을 이전 이동 횟수에서의 값들을 참조하여 계산
                    temp[i][j] = (
                        ((dp[i - 1][j] if i > 0 else 0 ) + (dp[i + 1][j] if i < m - 1 else 0)) % M + 
                        ((dp[i][j - 1] if j > 0 else 0) + (dp[i][j + 1] if j < n -1 else 0)) % M 
                    ) % M
                    
                
            dp = temp
            
        return count
        
        


