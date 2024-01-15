class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        # last_occurrence 딕셔너리는 {'b': 4, 'c': 3, 'a': 2}와 같이 생성됩니다. 
        stack = []

        for idx, char in enumerate(s):
             # 스택에 문자가 없는 경우
            if char not in stack:
                while stack and char < stack[-1] and idx < last_occurrence[stack[-1]]:
                    stack.pop()
                stack.append(char)
        
        return ''.join(stack)


