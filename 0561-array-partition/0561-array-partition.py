class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # nums 오름차순으로 소팅부터
        nums.sort()
        result = 0
        # 1,2,3,4
        for i in range(0,len(nums),2):
            result += nums[i]
            print(result)
        return result

        # 1,2,2,5,6,6

        # 이 코드는 각 쌍에서 작은 값들의 합을 최대화하는데, 
        # 정렬된 배열에서 짝수 번째 인덱스 값들을 합산하여 최대값을 구하는 방식으로 동작합니다.
