class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 각 문자의 등장 횟수릴 기록할 딕셔너리
        char_count = {}
        
        # 첫번째 순회: 각 문자의 등장 횟수 기록
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # 두번째 순회: 처음으로 등장하는 고유한 문자 찾기
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
        
        return -1
                