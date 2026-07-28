class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        mid = n//2
        if n==1:
            return s
        if n % 2 ==0:
            beg = "".join(sorted(s[:mid]))
            end = "".join(sorted(s[:mid],reverse = True))
            return beg + end
        else:
            beg = "".join(sorted(s[:mid]))
            end = "".join(sorted(s[:mid],reverse = True))
            return beg + s[mid] + end

        