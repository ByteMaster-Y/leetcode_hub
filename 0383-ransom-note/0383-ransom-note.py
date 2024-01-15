class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_map = {}
        magazine_map = {}

        for char in ransomNote:
            ransom_map[char] = ransom_map.get(char, 0) + 1 
       
        
        for char in magazine:
            magazine_map[char] = magazine_map.get(char, 0) + 1

        for char, count in ransom_map.items():
            if magazine_map.get(char, 0) < count:
                return False
        return True
