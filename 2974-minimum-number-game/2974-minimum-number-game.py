class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        arr = []

        for i in range(0, n-1, 2):
            nums[i] , nums [i + 1] = nums [i + 1] , nums[i]
        return nums
