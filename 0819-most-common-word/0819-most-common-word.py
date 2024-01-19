import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # \b: 단어 경계를 나타내는 메타 문자
        # \w+: 하나 이상의 알파벳 문자나 숫자에 일치.
        # paragraph에서 문자 추출
        words = re.findall(r'\b\w+\b', paragraph.lower())
        
        # most_common(1)은 Counter 객체에서 빈도가 가장 높은 항목을 1개 반환하는 메서드 
        # [0][0]은 이 결과에서 첫 번째 항목의 첫 번째 요소, 
        # 즉 가장 빈도가 높은 항목의 값을 가져오는 것입니다.
        words_count = Counter(word for word in words if word not in banned)
        
        return words_count.most_common(1)[0][0]
                