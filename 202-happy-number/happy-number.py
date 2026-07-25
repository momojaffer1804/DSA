class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        
        def sos(n):
            output = 0
            while n > 0 :
                digit = n %10
                output += digit**2
                n = n//10
            return output
        
        while n not in visit:
            visit.add(n)
            
            n = sos(n)
            if n ==1:
                return True
        return False
        
            
            
        