class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 이 코드는 입력된 리스트 nums에서 합이 0이 되는 모든 세 숫자의 조합을 찾습니다. 
        # 이 알고리즘은 입력 리스트를 먼저 정렬한 후, 
        # 투 포인터를 사용하여 합이 0이 되는 세 숫자 조합을 찾습니다. 
        # 겹치는 결과를 피하기 위해 중복된 숫자를 건너뛰는 부분이 추가되어 있습니다.
        # 알고리즘의 핵심 아이디어는 두 개의 포인터(left와 right)를 사용하여 합이 0이 되도록 조정하는 것입니다. 
        # 이를 통해 모든 유효한 조합을 찾고, 중복된 결과를 제거하여 반환합니다.
        nums.sort()
        # nums = [-4,-1,-1,0,1,2]
        result = []
        n = len(nums) # 6

        # 세개의 합이 0이 되는 부분
        for i in range(n-2):
            # 중복된 숫자 건너뛰기.
            # i > 0일 때 현재 값과 이전 값이 동일하면 중복된 숫자이므로 건너뜁니다.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # 중복된 숫자 건너뛰기
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1             
        return result
            
      