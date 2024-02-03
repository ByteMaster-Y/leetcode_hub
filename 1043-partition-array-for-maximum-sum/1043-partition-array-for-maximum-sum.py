class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        # 배열의 각 위치에 대해 최대 합을 계산합니다.
        for i in range(1, n + 1):
            max_val = float('-inf')

            # 현재 위치에서 가능한 부분 배열의 길이를 최대 길이 k로 제한하며 루프를 돕니다.
            for j in range(1, min(i, k) + 1):
                # 현재 부분 배열에서 최대값을 찾습니다.
                max_val = max(max_val, arr[i - j])

                # 현재 위치까지의 최대 합을 갱신합니다.
                dp[i] = max(dp[i], dp[i - j] + max_val * j)

        # 배열의 끝까지 고려한 최대 합을 반환합니다.
        return dp[n]
