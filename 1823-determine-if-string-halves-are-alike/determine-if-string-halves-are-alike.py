class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = 0
        b = 0
        n = len(s)
        vowel = ["a","e","i","o","u","A","E","I","O","U"]
        for i in range(n//2):
            if s[i] in vowel:
                a+=1
        for i in range(n//2 , n):
            if s[i] in vowel:
                b+=1

        return a==b

        