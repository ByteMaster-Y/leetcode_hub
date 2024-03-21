class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 문자열에서 알파벳과 숫자만을 추출하여 새로운 문자열 생성
        # isalnum()은 문자열 메서드로, 해당 문자열이 알파벳(a-z, A-Z) 또는 숫자(0-9)로만 이루어져 있는지 여부를 확인합니다. 
        # 만약 해당 문자열이 알파벳 또는 숫자로만 이루어져 있으면 True를 반환하고, 그렇지 않으면 False를 반환합니다.
        alphanumeric_s = ''.join(c.lower() for c in s if c.isalnum())

        # 생성된 문자열이 팰린드롬인지 검사
        left, right = 0, len(alphanumeric_s) - 1
        while left < right:
            if alphanumeric_s[left] != alphanumeric_s[right]:
                return False
            left += 1
            right -= 1
        return True