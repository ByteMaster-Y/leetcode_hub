class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}

        # 배열을 반복하면서 타겟에서 현재 숫자를 뺀 값을 딕셔너리에서 찾음.
        for i, num in enumerate(nums):
            # nums 배열을 인덱스와 값의 쌍으로 반복
            result = target - num
            if result in new_dict:
                # print([new_dict[result], i])
                return [new_dict[result], i]
                # 해당 숫자의 인덱스(num_dict[result])와 현재 숫자의 인덱스(i)를 반환하여 
                # 두 숫자의 합이 타겟이 되는 경우의 인덱스를 찾습니다.
            new_dict[num] = i
        return None