class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # T에 있는 각 문자의 등장 횟수를 저장하는 해시 맵
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        
        # 슬라이딩 윈도우 설정을 위한 포인터 및 결과 변수
        left, right = 0, 0
        min_len = float('inf')
        min_window_str = ""
        required_chars = len(t)
        
        while right < len(s):
            # 현재 문자를 윈도우에 추가
            if s[right] in t_count:
                t_count[s[right]] -= 1
                if t_count[s[right]] >= 0:
                    required_chars -= 1
            # 모든 문자가 포함된 경우
            while required_chars == 0:
                # 최소 윈도우 갱신
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window_str = s[left:right+1]
                # left를 이동하여 최소 윈도우 축소:
                if s[left] in t_count:
                    t_count[s[left]] += 1
                    if t_count[s[left]] > 0:
                        required_chars += 1
                left += 1
            # right를 이동하여 윈도우 확장
            right += 1
        return min_window_str
        
        