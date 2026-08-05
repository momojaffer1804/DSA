class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        prev_prev = 0
        for num in nums:
            temp = max(prev , prev_prev + num)
            prev_prev = prev
            prev = temp
        return prev
    


        