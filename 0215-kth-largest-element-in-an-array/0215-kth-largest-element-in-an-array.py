import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_heap = []
        
        for num in nums:
            heapq.heappush(k_heap,num)
            
            if len(k_heap) > k:
                heapq.heappop(k_heap)
                
        return k_heap[0]