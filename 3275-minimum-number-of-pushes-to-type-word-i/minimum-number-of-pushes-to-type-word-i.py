class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word)<=8:
            return len(word)
        elif len(word)<=16:
            rem = len(word)-8
            return (8+(2*rem))
        elif len(word)<=24:
            rem2 = len(word)-16
            return (24 + (3* rem2))
        elif len(word) ==25:
            return (52)
        elif len(word) ==26:
            return 56


        