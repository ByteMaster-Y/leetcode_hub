class Solution:
    def numberOfSteps(self, num: int) -> int:
        # Input: num = 14
        # Output: 6
        # 짝수/홀수 구분하기
        # 짝수면 계속 나누고 홀수면 하나 빼기
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num - 1
            steps += 1
        return steps
