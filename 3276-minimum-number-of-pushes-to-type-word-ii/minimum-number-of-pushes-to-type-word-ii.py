class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = [0] * 26
        for ch in word:
            counts[ord(ch) - ord('a')] += 1
        counts.sort(reverse = True)
        total = 0
        for idx, freq in enumerate(counts):
            if freq == 0:
                break
            total += freq * ((idx // 8) + 1)
        return total