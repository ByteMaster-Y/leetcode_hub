class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 결과를 저장할 집합
        result_set = set()

        # 첫 번째 배열을 집합으로 변환하여 중복 제거
        nums1_set = set(nums1)

        # 두 번째 배열을 순회하면서 공통 원소를 찾음
        for num in nums2:
            if num in nums1_set:
                result_set.add(num)

        return list(result_set)

                
            