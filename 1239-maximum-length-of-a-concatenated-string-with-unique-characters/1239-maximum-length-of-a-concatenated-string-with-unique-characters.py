class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_unique(combination):
            bitmask = 0
            for char in combination:
                char_bit = ord(char) - ord('a')
                if bitmask & (1 << char_bit) != 0:
                    return False
                bitmask |= (1 << char_bit)
            return True
        
        def backtrack(start, current):
            nonlocal max_length
            
            if is_unique(current):
                max_length = max(max_length, len(current))
                
            for i in range(start, len(arr)):
                backtrack(i+1, current + arr[i])
                
        max_length = 0
        backtrack(0,"")
        return max_length
        
                
                