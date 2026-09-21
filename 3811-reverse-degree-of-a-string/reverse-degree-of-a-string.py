class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i , c in enumerate(s):
            reverse = 26-(ord(c)-ord("a"))
            pos = i + 1

            total += reverse * pos
        return total 
        