class Solution:
    def myPow(self, x: float, n: int) -> float:
        is_negative = n < 0
        n = abs(n)
        res = 1.0
        
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
            
        return 1 / res if is_negative else res