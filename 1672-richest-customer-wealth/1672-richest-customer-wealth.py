class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # time complexcity O(nxm)
        # space complexcity O(1)

        # 각 고객의 자산 계산: 각 고객의 은행 계좌에 있는 돈의 합을 구하는 것이 필요합니다.
        # 배열에서 최댓값 찾기: 배열 내에서 최댓값을 찾아야 합니다.
        # 2차원 배열 순회: 2차원 배열을 행과 열에 걸쳐 순회하면서 요소들을 확인해야 합니다.

        max_wealth = 0 # 최댓값을 저장할 변수 초기화

        for i in range(len(accounts)):
            # print(sum(accounts[i]))
            current_wealth = sum(accounts[i])
            max_wealth = max(max_wealth, current_wealth)
        return max_wealth



        