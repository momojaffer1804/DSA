class Solution:
    def myPow(self, x: float, n: int) -> float:
        N = abs(n)
        ans = 1
        while N:
            if N %2 != 0:
                ans *= x
            
            x *= x
            N//=2

        if n <0:
            return 1/ans
        else:
            return ans
        