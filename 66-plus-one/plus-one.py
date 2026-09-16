class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = int("".join(str(digit) for digit in digits))

        final = result + 1
        digits_final = [int(d) for d in str(final)]
        return digits_final