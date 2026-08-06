class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range (1,11):
            prod = 1
            k = n
            while k:
                last = k % 10
                
                prod*=last
                k = k // 10
            if prod % t ==0:
                return n
            else:
                n +=1
                prod = 1
            
        