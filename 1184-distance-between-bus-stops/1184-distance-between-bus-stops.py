class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        clockwise_distance = sum(distance[min(start, destination):max(start, destination)])
        
        total_distance = sum(distance)
        counterclockwise_distance = total_distance - clockwise_distance
        
        return min(clockwise_distance, counterclockwise_distance)