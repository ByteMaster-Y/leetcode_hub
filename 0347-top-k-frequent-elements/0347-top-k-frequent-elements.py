from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Counter({1: 3, 2: 2, 3: 1})
        nums_counter = Counter(nums)
        
        # [(1, 3), (2, 2), (1, 2)]
        sorted_nums = sorted(nums_counter.items(), key=lambda x: x[1], reverse=True)
        
        result = [num for num, count in sorted_nums[:k]]
        
        return result
        