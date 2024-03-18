class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            # path 리스트의 복사본을 result 리스트에 추가하는 것을 의미합니다.
            result.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
            
        result = []
        backtrack(0, [])
        return result
        
        