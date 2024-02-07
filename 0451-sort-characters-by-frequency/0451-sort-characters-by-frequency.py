from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        # 문자열에서 각 문자의 빈도수를 카운트
        counter = Counter(s)
        
        # counter.items()는 Counter 객체의 메서드로, 각 문자와 해당 문자의 빈도수를 (문자, 빈도수) 쌍의 튜플 형태로 반환합니다. 
        # -x[-1]는 빈도수에 음수 부호를 붙여서 내림차순으로 정렬하도록 합니다.
        # x[0]은 문자열을 알파벳 순으로 정렬하는 데 사용됩니다. 
        sorted_char = sorted(counter.items(), key=lambda x: (-x[-1], x[0]))
        
        result = ''.join(char * freq for char, freq in sorted_char)
        
        return result