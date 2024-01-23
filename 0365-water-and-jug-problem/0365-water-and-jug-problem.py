import math
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        x =jug1Capacity
        y = jug2Capacity
        z = targetCapacity
        
        if x + y < z:
            return False
        
        if x == z or y == z or x + y == z:
            return True
        
        # GCD계산
        def gcd(a,b):
            while b:
                a, b = b, a % b 
            return a
        
        return z % gcd(x, y) == 0