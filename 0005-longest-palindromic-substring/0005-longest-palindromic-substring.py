class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s
        
        start, max_len = 0, 0
        
        for i in range(len(s)):
            # 홀수 길이 팰린드롬 검사
            l1 = self.expand_around_center(s, i, i)
            # 짝수 길이 팰린드롬 검사
            l2 = self.expand_around_center(s, i, i + 1)
            
            l = max(l1, l2)
            
            if l > max_len:
                max_len = l
                
                # 팰린드롬의 시작 인덱스 갱신
                start = i - (l - 1) // 2
        return s[start:start + max_len]
    
    def expand_around_center(self, s: str, left: int, right: int) -> int:
        # 팰린드롬을 양 옆으로 확장하는 함수
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1 # 포함되지 않는 길이 때문에 1을 추가적으로 뺀다.
