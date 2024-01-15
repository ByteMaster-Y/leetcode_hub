class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # 첫번째 숫자는 그냥 내려오고, 다음 숫자 부터는 처음부터 더해서 결과값 출력
        # time complexcity O(n)
        # space complexcity O(1)
      
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums
        
        

        
            
                
