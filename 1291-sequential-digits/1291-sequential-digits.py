class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        digits = "123456789"
        
        for length in range(len(str(low)), len(str(high)) + 1):
            for i in range(10 - length):
                num_str = digits[i:i+length]
                num = int(num_str)
                
                if low <= num <= high:
                    result.append(num)
                    
        return result