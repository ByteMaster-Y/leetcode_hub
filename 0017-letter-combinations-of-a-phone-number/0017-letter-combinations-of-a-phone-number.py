class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_map = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtracking(index, path):
            # 백트래킹 종료 조건: path가 완성되었을 때
            # index: 현재 처리 중인 숫자의 인덱스를 나타냅니다.
            # path: 지금까지 만들어진 문자 조합을 나타냅니다.

            if len(path) == len(digits): # -> 문자 조합이 완성
                combinations.append(''.join(path))
                return
            
            # 현재 숫자에 해당하는 문자들을 순회하며 백트래킹
            current_digit = digits[index]
            for char in phone_map[current_digit]: 
                path.append(char)
                # 다음 숫자로 이동하여 재귀 호출을 수행하는 부분
                backtracking(index + 1, path)
                path.pop()

        combinations = []
        backtracking(0, [])
        return combinations
